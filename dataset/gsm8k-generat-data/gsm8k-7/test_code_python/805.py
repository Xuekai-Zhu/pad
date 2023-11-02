def solution():
    num_screens = 6
    hours_open = 8
    movie_duration = 2

    # Calculate the number of movies that can be shown on each screen
    num_movies_per_screen = hours_open // (movie_duration * num_screens)

    # Calculate the total number of movies shown on all screens
    total_movies = num_screens * num_movies_per_screen

    result = total_movies
    return result

print(solution())