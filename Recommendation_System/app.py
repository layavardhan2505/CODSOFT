import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

movies = pd.read_csv("tmdb_5000_movies.csv")
def get_genres(text):
    genres = ast.literal_eval(text)
    return " ".join([g["name"] for g in genres])

movies["genres"] = movies["genres"].apply(get_genres)

cv = CountVectorizer(stop_words="english")
matrix = cv.fit_transform(movies["genres"])

similarity = cosine_similarity(matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    for i in range(len(movies)):
        if movies["title"][i].lower() == movie_name:

            scores = list(enumerate(similarity[i]))
            scores = sorted(scores, key=lambda x: x[1], reverse=True)

            print("\nTop Recommendations:\n")

            for movie in scores[1:6]:
                print(movies["title"][movie[0]])

            return

    print("Movie not found!")

movie = input("Enter Movie Name: ")
recommend(movie)