def solution():
    """Grandpa Lou enjoys watching movies on the Hallmark channel, where every movie lasts 90 minutes. If, on Tuesday, he watched several full-length movies on the Hallmark channel for a total of 4 hours and 30 minutes, and then on Wednesday he watched on the same channel twice as many movies as he did on Tuesday. What is the maximum number of full-length movies Grandpa could have watched during these two days?"""
    time_on_channel = 150
    time_on_channel_2 = time_on_channel * 2
    total_time = time_on_channel + time_on_channel_2
    movie_length = 90
    total_movies = total_time / movie_length
    result = total_movies
    return result

print(solution())