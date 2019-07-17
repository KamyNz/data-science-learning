from typing import List
import requests
import collections

# We did this to print type Movie record easily
# so we can have a list of records Type Movie
Movie = collections.namedtuple('Movie','imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score ',)

def find_movie_by_title(keyword: str) -> List[Movie]:
    url = f"http://movie_service.talkpython.fm/api/search/{keyword}"
    # this will work in >=3.5
    #print(url) #printing to see that is working
    resp = requests.get(url)
    resp.raise_for_status()
    
    #print(resp.text) # To check that is working 
    results = resp.json()
    #print(type(results),results) # To check the JSON
    
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r)) # Se tiene que poner Movie(**r) porque necesita saber que tipo de record

    return(movies)

