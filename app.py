import streamlit as st
import pandas as pd
import requests
import pickle

# Load the processed data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return movies[['title', 'movie_id']].iloc[movie_indices]


# Fetch movie poster from TMDB API
def fetch_poster(movie_id):

    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'

    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    try:
        response = requests.get(url, timeout=30)

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path

        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/300x450?text=Slow+Internet"


# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button('Recommend'):

    recommendations = get_recommendations(selected_movie)

    st.write("## Top 10 Recommended Movies")

    # Create 2 rows and 5 columns
    for i in range(0, 10, 5):

        cols = st.columns(5)

        for col, j in zip(cols, range(i, i + 5)):

            if j < len(recommendations):

                movie_title = recommendations.iloc[j]['title']

                movie_id = recommendations.iloc[j]['movie_id']

                poster_url = fetch_poster(movie_id)

                with col:
                    st.image(poster_url, width=130)

                    st.caption(movie_title)