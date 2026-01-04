import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

st.set_page_config(page_title="Movie Recommendation System")

st.title("🎬 AI Movie Recommendation System (K-Means)")
st.write("Movie recommendations using K-Means clustering")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")

movies = load_data()
movies['genres'] = movies['genres'].fillna("")

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(movies['genres'])

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
movies['cluster'] = kmeans.fit_predict(X)

# User input
movie_name = st.selectbox("Select a movie", movies['title'])

if st.button("Recommend"):
    cluster = movies[movies['title'] == movie_name]['cluster'].values[0]
    recommendations = movies[
        (movies['cluster'] == cluster) & (movies['title'] != movie_name)
    ]['title'].head(5)

    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write("👉", movie)
