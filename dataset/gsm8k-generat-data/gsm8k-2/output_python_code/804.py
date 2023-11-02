def solution():
    """A movie theater has 6 screens which show movies back-to-back all day. If the movie theater is open for 8 hours, and each movie lasts 2 hours, how many movies are shown in total throughout the day?"""
    num_screens = 6
    theater_hours = 8
    movie_duration = 2
    movies_per_screen = theater_hours // movie_duration
    total_movies = movies_per_screen * num_screens
    result = total_movies
    return result

print(solution())