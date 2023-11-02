def solution():
    """Grandpa Lou enjoys watching movies on the Hallmark channel, where every movie lasts 90 minutes. If, on Tuesday, he watched several full-length movies on the Hallmark channel for a total of 4 hours and 30 minutes, and then on Wednesday he watched on the same channel twice as many movies as he did on Tuesday. What is the maximum number of full-length movies Grandpa could have watched during these two days?"""
    tuesday_time = 4 * 60 + 30 # convert 4 hours and 30 minutes to minutes
    tuesday_movies = tuesday_time // 90
    wednesday_movies = 2 * tuesday_movies
    total_movies = tuesday_movies + wednesday_movies
    result = total_movies
    return result

print(solution())