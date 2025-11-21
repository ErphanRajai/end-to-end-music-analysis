# Spotify Hit Predictor: End-to-End Data Analysis

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboarding-yellow?logo=powerbi&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Data%20Cleaning-green?logo=microsoft-excel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)

### A Deep Dive into Music Popularity Trends

**Tools:** Excel (Cleaning) | Power BI (Dashboarding) | Python (Experimental ML)

---

## Project Overview

This project was created as a personal initiative to explore the data behind Spotify's massive library. As a music enthusiast and data practitioner, I wanted to answer a simple question: **What makes a song popular?**

Is it the tempo? The energy? Or is it simply who the artist is?

This repository documents my end-to-end workflow, starting from raw data cleaning in Excel, moving to in-depth visual analysis in Power BI, and concluding with a fun Machine Learning experiment to test if a computer could predict the next hit.

---

## Repository Structure

```
├── data/
│   └── spotify_songs.csv       # Raw and cleaned dataset
├── dashboards/
│   └── Spotify.pbix            # Interactive Power BI file
├── visuals/
│   ├── dashboard1.png          # Overview Screenshot
│   ├── dashboard2.jpg          # Granular View
│   ├── dashboard3.png          # Genre Tree Map
│   ├── plot1.png               # ML Feature Importance
│   ├── plot2.jpg               # Correlation Matrix
│   └── plot3.png               # Hits vs Flops Box Plot
├── notebooks/
│   └── prediction_model.py     # Python ML script
└── README.md
```
Here is your content organized into a clean, professional Markdown structure, ready for a portfolio or presentation.

# Music Data Analysis: From Excel to Machine Learning

## The Workflow

### 1. Data Cleaning (Excel)
* **Metadata:** Handled missing metadata and standardized genre labels.
* **Integrity:** Removed duplicate entries to ensure data integrity.
* **Feature Engineering:** Created initial calculated columns for "Decade" and "Duration Categories."

### 2. Data Analysis (Power BI)
* **Trends:** Explored historical trends and genre dominance.
* **Metrics:** Visualized key metrics (BPM, Danceability) across different playlists.

### 3. Predictive Modeling (Python - Bonus)
* **Model:** Trained a Random Forest model to determine if audio features could predict a song's "Popularity Score."

---

## Part 1: Data Analysis & Visualization
**Focus:** Exploratory Data Analysis (EDA) using Power BI

### 1. The Big Picture: Artists & Trends
My first dashboard focuses on the macro trends. I analyzed the Top 10 Artists based on average popularity and how music popularity scores have fluctuated over the decades.

> **Figure 1:** High-level overview of artist performance and temporal trends.

**Key Insights:**
* **Genre Dominance:** Pop, Latin, and EDM are the most prevalent genres in the dataset.
* **The "Recency" Effect:** As seen in the "Average Popularity by Release Year" chart, there is a distinct trend where newer songs (post-2010) have different popularity distributions compared to classics from the 60s/70s.
* **Top Performers:** Artists like Trevor Daniel and Y2K topped the average popularity charts in this specific dataset snapshot.

### 2. Genre Distribution
I dug deeper into how genres are distributed across playlists. This helps understand the composition of the dataset and potential biases towards specific subgenres.

> **Figure 2:** Tree map visualizing the density of sub-genres.

**Insight:** Categories like "Indie Poptimism" and "Electro House" show significant counts, indicating the dataset is heavily skewed towards modern, electronic-influenced music.

### 3. Granular Track View
A detailed view allowing for the inspection of individual track metrics such as BPM (Tempo), Danceability, and Energy. This view was designed for data exploration, allowing the user to filter tracks that meet specific criteria (e.g., "High Energy" + "Low Acousticness").

> **Figure 3:** Tabular view for filtering specific track attributes.

---

## Part 2: Machine Learning Experiment
**Focus:** Random Forest Regression & Classification *(Done for fun!)*

Out of curiosity, I took the analyzed data into Python to see if a machine could learn the patterns I saw in Power BI. I trained a Random Forest Regressor to predict the Track Popularity Score (0-100).

### 1. What actually drives popularity?
After training the model, I used Feature Importance to understand what the model found most valuable.

> **Figure 4:** Random Forest Feature Importance ranking.

**The "Artist" Revelation:**
The model revealed a fascinating truth: `track_artist_encoded` (The Artist's Reputation) is by far the most important predictor. Audio features like loudness, tempo, and danceability matter, but they are secondary to *who* is releasing the song.

### 2. Audio Correlations
I checked for multicollinearity to ensure the model wasn't using redundant features.

> **Figure 5:** Correlation heatmap of audio features.

**Insight:** There is a strong negative correlation between energy and acousticness. High-energy tracks tend to be less acoustic (electronic), which aligns with the Pop/EDM dominance found in the Power BI analysis.

### 3. Hits vs. Flops
To visualize the difference between a "Hit" (Popularity > 70) and a "Flop" (Popularity < 30), I compared their audio profiles.

> **Figure 6:** Box plots comparing audio features of Hits vs. Flops.

**Insight:** "Hits" (Orange box) tend to be consistently louder (higher dB) and have a tighter distribution of Danceability compared to Flops.

---

## Future Improvements
If I were to expand this project, I would consider:

1.  **Lyrics NLP:** Integrating a Natural Language Processing model to analyze sentiment in song lyrics.
2.  **External Data:** Incorporating social media trends (TikTok/Twitter) to account for viral marketing, which the current audio-only model misses.
3.  **Time Series:** Predicting future popularity trends based on seasonality.

## Conclusion
This project demonstrated that while audio features provide some signal, the music industry is heavily driven by **Artist Brand**. The model achieved an $R^2 \approx 0.60$, suggesting that 40% of a song's success is determined by external factors (marketing, trends, luck) not present in the audio data.

## Tech Stack
* **Microsoft Excel:** Data Cleaning & Preprocessing.
* **Microsoft Power BI:** Dashboarding & Visualization.
* **Python:** Data Science & ML.
* **Libraries:** Pandas, Scikit-Learn, Seaborn, Matplotlib.

> *Note: This project was created for educational purposes and personal enjoyment.*

---

**Next Step:** Would you like me to help you write a **GitHub README** or a **LinkedIn post** to promote this project?
