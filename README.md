## 🎦Movie Recommendation System
This repository contains a movie recommendation system built using Python, Pandas, Scikit-Learn, and Streamlit. The system recommends movies based on their similarity to a given movie using a combination of collaborative filtering and content-based filtering.

## Overview
The movie recommendation system aims to predict or filter preferences according to user choices. It is used in various areas such as movies, music, news, books, and more. This system utilizes two main approaches:

1. `Collaborative Filtering`: Builds a model based on the user's past behavior and similar decisions made by other users.
2. `Content-Based Filtering`: Uses a series of discrete characteristics of an item to recommend additional items with similar properties.

## Data
The data used in this project comes from the TMDB 5000 Movie Dataset. It includes two main files:

- tmdb_5000_credits.csv
- tmdb_5000_movies.csv

These datasets contain information about movies, such as their cast, crew, genres, and keywords.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/anilkumar5590/movie-recommendation-system.git
cd movie-recommendation-system
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Download the dataset files and place them in the repository directory.
4. Obtain an API key from TMDB and replace `YOUR_API_KEY` in the fetch_poster function within the movie.py file.

## Usage
To use the interactive movie recommendation system, run the Streamlit application:
1. Run the Streamlit App:
```bash
streamlit run movie.py
```
If the above command shows errors then use the below command
```bash
python -m streamlit run movie.py
```
2. Using the App:
- Select or enter a movie name in the dropdown.
- Click the "Recommend" button to get a list of recommended movies with posters.

## Notebook Description
The Jupyter notebook Movie_Recommendation_System_Notebook.ipynb contains the following steps:

1. Import Libraries and Load Data: Load necessary libraries and datasets.
2. Data Preprocessing: Clean and preprocess the data, including handling missing values and converting columns to the correct format.
3. Feature Extraction: Extract relevant features from the data.
4. Vectorization: Convert textual data into numerical vectors using CountVectorizer.
5. Similarity Calculation: Compute cosine similarity between movie vectors.
6. Recommendation Function: Define a function to recommend movies based on similarity.
7. Saving Models: Save the processed data and similarity matrix using pickle.

To run the notebook, execute the cells in order.

## Model Explanation
#### 1. Data Preprocessing
- Genres: Extract and convert genres from JSON format.
- Keywords: Extract and convert keywords from JSON format.
- Cast: Extract the top 5 cast members.
- Crew: Extract the director's name.
#### 2. Feature Engineering
- Tags: Combine genres, keywords, cast, and crew into a single feature.
#### 3. Vectorization
- CountVectorizer: Convert text data into a matrix of token counts, limited to the top 5000 features.
#### 4. Similarity Calculation
- Cosine Similarity: Compute the cosine similarity between movie vectors to measure their similarity.
#### 5. Recommendation
- Function: Given a movie name, find similar movies based on cosine similarity scores and fetch their posters.

## Preview
https://github.com/anilkumar5590/movie-recommendation-system/assets/132257668/cedac699-629b-4d05-8514-da4af4981910


## 🔗 Follow us
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anilkumarkonathala/)

## Feedback
If you have any feedback, please reach out to us at konathalaanilkumar143@gmail.com



