def solution():
    """A movie theater has 6 screens which show movies back-to-back all day. If the movie theater is open for 8 hours, and each movie lasts 2 hours, how many movies are shown in total throughout the day?"""
    # Define the number of screens, hours of operation, and movie duration
    screens = 6
    hours = 8
    movie_duration = 2

    # Calculate the number of movies that can be shown on each screen
    movies_per_screen = hours // movie_duration

    # Calculate the total number of movies shown across all screens
    total_movies = screens * movies_per_screen

    # Return the result
    result = total_movies
    return result

print(solution())