def solution():
    num_screens = 6  # The movie theater has 6 screens
    hours_open = 8  # The movie theater is open for 8 hours
    movie_duration = 2  # Each movie lasts for 2 hours

    # Calculate the number of movies shown on each screen
    movies_per_screen = hours_open // movie_duration

    # Calculate the total number of movies shown on all screens
    total_movies = num_screens * movies_per_screen

    result = total_movies
    return result

print(solution())