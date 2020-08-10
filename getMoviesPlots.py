import requests
import json
from imdb import IMDb, IMDbDataAccessError

def get_movies():
  movies = []
  i = 1
  while i < 501:
    x = requests.get('http://api.themoviedb.org/3/genre/10751/movies?api_key=09bd8e6de518232b5fd642cb85657a3c&page='+str(i))
    response = x.text

    res = json.loads(response)
    for movie in res['results']:
      movies.append(movie['title'])
    i+=1

  print("--------done get family Movies--------")
  return movies

familyMovies = get_movies()

plots = []
for movie in familyMovies:
  name = movie.replace(" ", "+")
  x = requests.get('http://www.omdbapi.com/?t='+name+'&plot=full&apiKey=7ba7385b')
  response = x.text
  if ("Error" in response):
        continue
  res = json.loads(response)
  plots.append(res["Plot"])
open("./" + "moviesPlots.json", "w").write(json.dumps(plots, indent=4))