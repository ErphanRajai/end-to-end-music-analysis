import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler

# --- PAGE CONFIG ---
st.set_page_config(page_title="Spotify Hit Predictor", page_icon="🎵")

# --- HEADER ---
st.title("🎵 Spotify Song Popularity Predictor")
st.write("Tweaking audio features to see if your song will be a Hit or a Flop!")

# --- 1. LOAD & TRAIN (Cached for Speed) ---
@st.cache_resource
def load_and_train_model():
    # Load Data
    try:
        df = pd.read_csv("spotify_songs.csv", encoding='latin-1')
    except:
        st.error("Could not find 'spotify_songs.csv'. Please make sure it's in the same folder.")
        return None, None, None

    # Cleaning & Engineering (Same logic as your notebook)
    df = df.dropna(subset=['Track Popularity Score'])
    df['Energy_Acoustic_Interaction'] = df['energy'] * (1 - df['acousticness'])
    epsilon = 1e-6
    df['Loudness_Per_Duration'] = df['loudness'] / (df['Duration_Min'] + epsilon)
    
    # Artist Encoding
    artist_avg = df.groupby('track_artist')['Track Popularity Score'].mean().to_dict()
    df['track_artist_encoded'] = df['track_artist'].map(artist_avg)
    
    # Fill missing artists with global average
    global_mean = df['Track Popularity Score'].mean()
    df['track_artist_encoded'] = df['track_artist_encoded'].fillna(global_mean)

    # Features
    features = ['track_artist_encoded', 'Release Year', 'tempo', 'liveness', 'valence',
                'speechiness', 'Danceability', 'loudness', 'Loudness_Per_Duration',
                'acousticness', 'Duration_Min', 'energy', 'Energy_Acoustic_Interaction']
    
    X = df[features].copy()
    y = df['Track Popularity Score']
    
    # Scaling
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train Model (Fast version)
    model = RandomForestRegressor(n_estimators=100, max_depth=20, random_state=42, n_jobs=-1)
    model.fit(X_scaled, y)
    
    return model, scaler, artist_avg

model, scaler, artist_avg = load_and_train_model()

if model is not None:
    # --- SIDEBAR INPUTS ---
    st.sidebar.header("🎚️ Adjust Song Features")
    
    # Artist Input (The most important feature!)
    artist_name = st.sidebar.text_input("Artist Name", "Ed Sheeran")
    
    # Audio Features Sliders
    release_year = st.sidebar.slider("Release Year", 1980, 2025, 2023)
    danceability = st.sidebar.slider("Danceability", 0.0, 1.0, 0.7)
    energy = st.sidebar.slider("Energy", 0.0, 1.0, 0.8)
    acousticness = st.sidebar.slider("Acousticness", 0.0, 1.0, 0.1)
    loudness = st.sidebar.slider("Loudness (dB)", -60.0, 0.0, -5.0)
    tempo = st.sidebar.slider("Tempo (BPM)", 50, 200, 120)
    duration_min = st.sidebar.slider("Duration (Mins)", 1.0, 10.0, 3.5)
    valence = st.sidebar.slider("Valence (Happiness)", 0.0, 1.0, 0.6)
    speechiness = st.sidebar.slider("Speechiness", 0.0, 1.0, 0.05)
    liveness = st.sidebar.slider("Liveness", 0.0, 1.0, 0.1)
    
    # --- PREDICTION LOGIC ---
    if st.button("Predict Popularity"):
        # 1. Handle Artist Encoding
        # If artist exists in training data, use their avg score. If not, use 50 (neutral).
        artist_score = artist_avg.get(artist_name, 50.0) 
        
        # 2. Engineer Features
        interaction = energy * (1 - acousticness)
        loudness_per_duration = loudness / (duration_min + 1e-6)
        
        # 3. Create Dataframe
        input_data = pd.DataFrame([[
            artist_score, release_year, tempo, liveness, valence,
            speechiness, danceability, loudness, loudness_per_duration,
            acousticness, duration_min, energy, interaction
        ]], columns=['track_artist_encoded', 'Release Year', 'tempo', 'liveness', 'valence',
                     'speechiness', 'Danceability', 'loudness', 'Loudness_Per_Duration',
                     'acousticness', 'Duration_Min', 'energy', 'Energy_Acoustic_Interaction'])
        
        # 4. Scale
        input_scaled = scaler.transform(input_data)
        
        # 5. Predict
        prediction = model.predict(input_scaled)[0]
        
        # --- DISPLAY RESULT ---
        st.metric(label="Predicted Popularity Score", value=f"{prediction:.1f} / 100")
        
        if prediction > 80:
            st.balloons()
            st.success("🔥 This song is likely to be a HIT!")
        elif prediction > 50:
            st.info("⚠️ This is an AVERAGE performing track.")
        else:
            st.error("📉 This track might struggle to gain traction.")
            
        # Interpretation
        st.markdown("### 🧠 Model Logic")
        if artist_score > 75:
            st.write(f"- **Major Boost:** {artist_name} is a superstar, significantly lifting the score.")
        elif artist_score < 40:
             st.write(f"- **Drag Factor:** {artist_name} is relatively unknown or niche.")
             
        st.write(f"- **Energy/Acoustic Mix:** {interaction:.2f} (Higher is usually better for Pop/EDM)")