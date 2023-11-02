def solution():
    """A movie theater has 6 screens which show movies back-to-back all day. If the movie theater is open for 8 hours, and each movie lasts 2 hours, how many movies are shown in total throughout the day?"""
    # Define the number of screens and hours the theater is open
    SCREENS = 6
    HOURS_OPEN = 8

    # Calculate the number of movies shown on each screen
    movies_per_screen = HOURS_OPEN // 2

    # Calculate the total number of movies shown throughout the day
    total_movies = SCREENS * movies_per_screen

    # Display the total number of movies shown
    result = total_movies
    return result

print(solution())