def solution():
    """Grandpa Lou enjoys watching movies on the Hallmark channel, where every movie lasts 90 minutes.  If, on Tuesday, he watched several full-length movies on the Hallmark channel for a total of 4 hours and 30 minutes, and then on Wednesday he watched on the same channel twice as many movies as he did on Tuesday.  What is the maximum number of full-length movies Grandpa could have watched during these two days?"""
    
    # Define the total time Grandpa watched movies
    total_time = 4 * 60 + 30  # in minutes

    # Calculate the maximum number of movies Grandpa could watch on Tuesday
    tuesday_movies = total_time // 90

    # Calculate the maximum number of movies Grandpa could watch on Wednesday
    wednesday_movies = tuesday_movies * 2

    # Calculate the maximum number of movies Grandpa could watch in total
    total_movies = tuesday_movies + wednesday_movies

    result = total_movies
    return result

print(solution())