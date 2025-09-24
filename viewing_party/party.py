# ------------- WAVE 1 --------------------
#1

WATCH_LIST = "watchlist"
WATCHED = "watched"
FRIEND_DATA = "friends"
SUBSCRIPTIONS = "subscriptions"
FAVORITES = "favorites"

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
    # changed this from if watched is none
    if not watched:
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
        
    



# ------------- WAVE 3 --------------------
# none of the friends watched these movies
# only user wanted it 
def get_unique_watched(user_data):
    # access data
    watched = user_data.get(WATCHED, [])
    friends = user_data.get(FRIEND_DATA, [])

    # all the movies all the friends watched 
    # each movie as a single string 
    friends_watched = []
    for friend in friends:
        friends_watched.extend(friend.get(WATCHED, []))
    
    # get user unique movies
    # add the movie to the list 
    # if its not in the friend's watched list
    user_unique_watched = []
    for movie in watched:
        if movie not in friends_watched:
            user_unique_watched.append(movie)
    return user_unique_watched


    
# only friends watched the movies, not the user
def get_friends_unique_watched(user_data):
    # access data
    watched = user_data.get(WATCHED, [])
    friends = user_data.get(FRIEND_DATA, [])

    # all the movies all the friends watched 
    # each movie as a single string 
    # duplicate codes with the previous function
    # can create helper function
    friends_watched = []
    for friend in friends:
        friends_watched.extend(friend.get(WATCHED, []))   

    # eliminate the duplicated movies   
    # from the list above with all the movies all the friends watched
    # eliminates to duplicated ones
    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in friends_unique_watched:
            friends_unique_watched.append(movie)

    # for the movie that the friends watched
    # if the movie is not in the user's watched list
    # meaning user did not watch it yet
    only_friends_watched_not_user = []
    for movie in friends_unique_watched:
        if movie not in watched:
            only_friends_watched_not_user.append(movie)
    return only_friends_watched_not_user




    



        

# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    # access data
    watched = user_data.get(WATCHED, [])
    friends = user_data.get(FRIEND_DATA, [])
    subscriptions = user_data.get(SUBSCRIPTIONS, [])
    
    # this is duplicated code from WAVE 3
    # all the movies all the friends watched 
    # each movie as a single string 
    # duplicate codes with the previous function
    # can create helper function
    friends_watched = []
    for friend in friends:
        friends_watched.extend(friend.get(WATCHED, []))   

    # this is duplicated code from WAVE 3
    # eliminate the duplicated movies   
    # from the list above with all the movies all the friends watched
    # eliminates to duplicated ones
    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in friends_unique_watched:
            friends_unique_watched.append(movie)
    
    # recommended is movies that friends watched but user have not
    # and in user's subscriptions
    recommended_movies = []
    for movie in friends_unique_watched:
        if movie not in watched and movie.get("host") in subscriptions:
            recommended_movies.append(movie)
    return recommended_movies


# ------------- WAVE 5 --------------------

# conditions: user not watched, friend watched
# is user's most frequent watched genre
def get_new_rec_by_genre(user_data):
    # access data
    watched = user_data.get(WATCHED, [])
    friends = user_data.get(FRIEND_DATA, [])
    most_watched_genre = get_most_watched_genre(user_data)
    
    # this is duplicated code from WAVE 3
    # all the movies all the friends watched 
    # each movie as a single string 
    # duplicate codes with the previous function
    # can create helper function
    friends_watched = []
    for friend in friends:
        friends_watched.extend(friend.get(WATCHED, []))   

    # this is duplicated code from WAVE 3
    # eliminate the duplicated movies   
    # from the list above with all the movies all the friends watched
    # eliminates to duplicated ones
    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in friends_unique_watched:
            friends_unique_watched.append(movie)
    
    # recommended is movies that friends watched but user have not
    # and in user's subscriptions
    # most watch genre is from wave_2
    # 
    recommended_movies_by_genre = []
    for movie in friends_unique_watched:
        if movie not in watched and movie["genre"] == most_watched_genre:
            recommended_movies_by_genre.append(movie)
    return recommended_movies_by_genre







# user's favoraite, friend not watched
def get_rec_from_favorites(user_data):
    # access data
    watched = user_data.get(WATCHED, [])
    friends = user_data.get(FRIEND_DATA, [])
    favorites = user_data.get(FAVORITES, [])
    
    # this is duplicated code from WAVE 3
    # all the movies all the friends watched 
    # each movie as a single string 
    # duplicate codes with the previous function
    # can create helper function
    friends_watched = []
    for friend in friends:
        friends_watched.extend(friend.get(WATCHED, []))   

    # this is duplicated code from WAVE 3
    # eliminate the duplicated movies   
    # from the list above with all the movies all the friends watched
    # eliminates to duplicated ones
    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in friends_unique_watched:
            friends_unique_watched.append(movie)
    
    # recommended is movies user favorite, but friend not watch
    recommended_favorite_movies_to_friends = []
    for movie in favorites:
        # if friends did watch the movie
        if movie not in friends_unique_watched:
            # we will add it to our list to recommend to friend
            recommended_favorite_movies_to_friends.append(movie)
    return recommended_favorite_movies_to_friends


