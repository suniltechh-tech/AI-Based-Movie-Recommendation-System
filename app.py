import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(page_title="Movie Recommendation System", layout="centered")

st.title("🎬 AI-Based Movie Recommendation System")
st.write("Get movie recommendations based on your favorite movie.")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")

movies = load_data()

# Fill missing values
movies['genres'] = movies['genres'].fillna('')

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend(movie_title, num_recommendations=5):
    if movie_title not in movies['title'].values:
        return None

    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]

    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

# User input
movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(movie_name)

    if recommendations is not None:
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write("👉", movie)
    else:
        st.error("Movie not found in dataset.")
