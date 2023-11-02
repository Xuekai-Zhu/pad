def solution():
    """A movie theater has 6 screens which show movies back-to-back all day. If the movie theater is open for 8 hours, and each movie lasts 2 hours, how many movies are shown in total throughout the day?"""
    screens = 6
    hours_open = 8
    movie_length = 2
    movies_per_screen = hours_open // movie_length
    total_movies = movies_per_screen * screens
    result = total_movies
    return result

print(solution())