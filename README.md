## 📖 Project Explanation

The Movie Recommendation System is a machine learning based web application that recommends similar movies to users based on their selected movie. The main objective of this project is to help users discover movies easily using recommendation techniques similar to platforms like Netflix and Amazon Prime.

This project is developed using Python, Pandas, Scikit-learn, and Streamlit. The movie dataset is collected from Kaggle, and movie posters are fetched using the TMDB API.

The recommendation system uses the Content-Based Filtering technique. Movies are recommended based on similarities between movie features such as genres, keywords, cast, crew, and movie overview. These features are combined into a single text format and converted into vectors using CountVectorizer from Scikit-learn.

After vectorization, Cosine Similarity is applied to calculate similarity scores between movies. When a user selects a movie, the system compares similarity scores and recommends the top 10 most similar movies.

The frontend of the project is built using Streamlit, which provides a simple and interactive web interface. Users can select a movie from the dropdown menu, and the application displays recommended movie titles along with their posters.

---

## 🛠️ Technologies Used

- Python  
  https://www.python.org/

- Pandas  
  https://pandas.pydata.org/

- NumPy  
  https://numpy.org/

- Scikit-learn  
  https://scikit-learn.org/

- Streamlit  
  https://streamlit.io/

- Requests Library  
  https://requests.readthedocs.io/

- TMDB API  
  https://www.themoviedb.org/

- Kaggle Dataset  
  https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 🔗 Project Links

- GitHub Repository  
  https://github.com/gangadhar3123/Movie-Recommendation-System

- Kaggle Dataset  
  https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
