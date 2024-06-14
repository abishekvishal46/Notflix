import imdb
import concurrent.futures

import imdb
import concurrent.futures

def fetch_movie_img_url(movie_title):
    ia = imdb.IMDb()
    search_results = ia.search_movie(movie_title)
    movie = search_results[0]
    ia.update(movie)
    return movie.get('full-size cover url')
mcu = [
    "Harry Potter and the Sorcerer's Stone (2001)",
    "Harry Potter and the Chamber of Secrets (2002)",
    "Harry Potter and the Prisoner of Azkaban (2004)",
    "Harry Potter and the Goblet of Fire (2005)",
    "Harry Potter and the Order of the Phoenix (2007)",
    "Harry Potter and the Half-Blood Prince (2009)",
    "Harry Potter and the Deathly Hallows: Part 1 (2010)",
    "Harry Potter and the Deathly Hallows: Part 2 (2011)"
]
imgs = {}
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(fetch_movie_img_url, movie_title): movie_title for movie_title in mcu}
    for future in concurrent.futures.as_completed(futures):
        movie_title = futures[future]
        img_url = future.result()
        imgs[movie_title] = img_url
print(imgs)



