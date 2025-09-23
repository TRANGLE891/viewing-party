# ------------- WAVE 1 --------------------
#1

WATCH_LIST = "watchlist"
WATCHED = "watched"

def create_movie(title, genre, rating):
    if title is None:
        return None
    if genre is None:
        return None
    if rating is None:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }
#2
def add_to_watched(input_user_data, movie):
    user_data = input_user_data.copy()
    if user_data.get(WATCHED) is not None:
        user_data[WATCHED].append(movie)
    return user_data
#3
def add_to_watchlist(user_data, movie):
    if user_data.get(WATCH_LIST) is not None:
        user_data[WATCH_LIST].append(movie)
    return user_data
# 4
def watch_movie(user_data, title):
    if user_data.get(WATCHED) is None:
        return user_data
    if user_data.get(WATCH_LIST) is None:
        return user_data

    for movie in user_data[WATCH_LIST]:
        if movie["title"] == title:
            user_data[WATCH_LIST].remove(movie)
            user_data[WATCHED].append(movie)
    return user_data
                            
# ------------- WAVE 2 --------------------
# 1
def get_watched_avg_rating(user_data):
    watched = user_data.get(WATCHED, [])
    if watched is None:
        return 0.0
    total_rating = 0
    for movie in watched:
        total_rating += movie["rating"]
    avg_rating = total_rating/len(watched)
    return avg_rating
#2
def get_most_watched_genre(user_data):
    watched = user_data.get(WATCHED, [])
    if watched is None:
        return 0.0
    count_genre ={}
    for movie in watched:
        genre = movie["genre"]
        count_genre[genre] = count_genre.get(genre,0) +1
    most_watched_genre = None
    highest_count = 0
    for genre in count_genre:
        if count_genre[genre] > highest_count:
            highest_count = count_genre[genre]
            most_watched_genre = genre
    return most_watched_genre
        
    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

