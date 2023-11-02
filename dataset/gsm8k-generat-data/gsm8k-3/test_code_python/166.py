def solution():
    """Grandpa Lou enjoys watching movies on the Hallmark channel, where every movie lasts 90 minutes. If, on Tuesday, he watched several full-length movies on the Hallmark channel for a total of 4 hours and 30 minutes, and then on Wednesday he watched on the same channel twice as many movies as he did on Tuesday. What is the maximum number of full-length movies Grandpa could have watched during these two days?"""
    # Define the duration of a full-length movie in minutes
    MOVIE_DURATION = 90

    # Calculate the total duration of movies watched on Tuesday in minutes
    tuesday_duration = 4 * 60 + 30

    # Calculate the total number of movies watched on Tuesday
    tuesday_movies = tuesday_duration // MOVIE_DURATION

    # Calculate the total number of movies watched on Wednesday
    wednesday_movies = 2 * tuesday_movies

    # Calculate the maximum number of full-length movies Grandpa could have watched
    max_movies = tuesday_movies + wednesday_movies

    result = max_movies
    return result

print(solution())