from flask import render_template, request
from movie_website import app  # Import the Flask app instance created in __init__.py
import imdb

from movie_dict import mcu_movies, dc_movies, pirates_of_the_caribbean, harry_potter_movies
from series_dict import love, comedy, fantasy, anime

def related_search(movie_title):
    ia = imdb.IMDb()
    search_results = ia.search_movie(movie_title)
    if not search_results:
        return -1
    movie = search_results
    return movie

@app.route("/")
def index():
    return render_template('index.html', mcu=mcu_movies, dc=dc_movies, poc=pirates_of_the_caribbean,hp=harry_potter_movies)

def movie_info(movie_id):
    ia = imdb.IMDb()
    movie = ia.get_movie(movie_id)
    if not movie:
        print(f"Movie with ID {movie_id} not found.")
        return None
    ia.update(movie)
    name = movie.get('title')
    release_date = movie.get('original air date')
    cast = movie.get('cast')
    synopsis = movie.get("plot outline")
    cast_name = [person["name"] for person in cast]
    directors = movie.get('directors', [])
    ratings = movie.get("rating")
    director_names = [person['name'] for person in directors]
    poster = movie['full-size cover url']
    movie_id = movie.movieID
    return ratings, release_date, cast_name, director_names, synopsis, poster, movie_id, name

@app.route("/movieso", methods=["POST", "GET"])
def movieso():
    movie_name = request.args.get('movie_name')
    m_id = request.args.get('movie_id')
    print(m_id)
    if movie_name is not None:
         a, b, c, d, e, i, m_idi, name = movie_info(int(m_id))
         return render_template("video_player.html", a=a, b=b, c=c, d=d, e=e, i=i, movie_id=m_id, movie_n=name,mode="movie")
    return render_template('index.html', mcu=mcu_movies, dc=dc_movies, poc=pirates_of_the_caribbean, hp=harry_potter_movies)

@app.route("/searches", methods=["POST", "GET"])
def searches():
    global mode
    if request.method == "POST":
        results = {}
        movie_name = request.form.get("movie_name")
        ia = imdb.IMDb()
        result_imdb = related_search(movie_name)

        for movie in result_imdb[:2]:
            ia.update(movie)
            poster = movie.get('full-size cover url')
            movie_id = movie.movieID
            print(movie_id)
            if movie['kind'] == 'movie':
                mode = "movies"
            else:
                mode = "series"
            print(movie["kind"])
            results[movie] = [poster, mode, movie_id]

        return render_template("search.html", search_results=results)

@app.route("/serieso", methods=["POST", "GET"])
def serieso():
    movie_name = request.args.get('movie_name')
    m_id = request.args.get('movie_id')
    print(m_id)
    if movie_name is not None:
        a, b, c, d, e, i, m_id, name = movie_info(int(m_id))
        return render_template("video_player.html", a=a, b=b, c=c, d=d, e=e, i=i, movie_id=m_id, movie_n=name,
                               mode="tv")

    return render_template("series.html", love=love, comedy=comedy, fantasy=fantasy,anime=anime)
