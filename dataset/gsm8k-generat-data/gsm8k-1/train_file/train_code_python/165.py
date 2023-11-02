def solution():
    """Grandpa Lou enjoys watching movies on the Hallmark channel, where every movie lasts 90 minutes. If, on Tuesday, he watched several full-length movies on the Hallmark channel for a total of 4 hours and 30 minutes, and then on Wednesday he watched on the same channel twice as many movies as he did on Tuesday. What is the maximum number of full-length movies Grandpa could have watched during these two days?"""
    tuesday_minutes = 270
    wednesday_minutes = 2 * tuesday_minutes
    total_minutes = tuesday_minutes + wednesday_minutes
    movies_watched = total_minutes / 90
    result = int(movies_watched)
    return result

print(solution())