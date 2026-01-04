🎬 AI-Based Movie Recommendation System using K-Means Clustering
📌 Introduction

The AI-Based Movie Recommendation System is a machine learning project designed to recommend movies to users based on similarity in movie genres.
The system applies K-Means clustering to group similar movies together and suggests recommendations from the same cluster.

This project demonstrates the practical use of unsupervised machine learning, text vectorization, and web application development using Streamlit.

🎯 Objective

The main objectives of this project are:

To build a movie recommendation system using machine learning

To understand and apply K-Means clustering

To recommend movies based on content similarity

To create a simple and interactive user interface

🛠️ Technologies and Tools Used

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn

Machine Learning Algorithm: K-Means Clustering

Text Processing: TF-IDF Vectorization

Web Framework: Streamlit

🧠 System Architecture & Workflow

Movie data is loaded from a CSV file

Movie genres are preprocessed and cleaned

Genres are converted into numerical vectors using TF-IDF

K-Means clustering groups similar movies

User selects a movie from the interface

System recommends movies from the same cluster

📂 Dataset Description

The dataset used in this project is a CSV file (movies.csv) containing:

Title: Name of the movie

Genres: Categories associated with the movie

This dataset is lightweight and suitable for demonstrating clustering-based recommendations.

📁 Project Structure
AI-Based-Movie-Recommendation-System/
│
├── app.py               # Streamlit web application
├── movies.csv           # Movie dataset
├── requirements.txt     # Required Python libraries
├── README.md            # Project documentation

⚙️ Machine Learning Model

Algorithm: K-Means Clustering

Type: Unsupervised Learning

Feature Extraction: TF-IDF Vectorizer

Similarity Logic: Movies in the same cluster are considered similar

The model does not require labeled data, making it suitable for exploratory and recommendation tasks.

▶️ How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/suniltechh-tech/AI-Based-Movie-Recommendation-System.git
cd AI-Based-Movie-Recommendation-System

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Application
streamlit run app.py

💡 Key Features

Genre-based movie recommendations

Simple and user-friendly interface

Fast and efficient clustering

Easy to extend with larger datasets

📊 Output Example

User selects Inception

System recommends movies like:

Interstellar

The Matrix

Avengers

🚀 Future Enhancements

Use large-scale datasets (MovieLens / TMDB)

Add movie posters and ratings

Automatically determine optimal K value

Improve UI design

Deploy as a public web application

🧑‍💻 Author
