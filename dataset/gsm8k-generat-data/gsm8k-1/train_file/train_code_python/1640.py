def solution():
    """John uses the bathroom every 50 minutes. How many times does he use the bathroom during a 2.5-hour movie?"""
    movie_length = 2.5 * 60 #convert to minutes
    bathroom_time = 50
    times_used = movie_length // bathroom_time
    result = times_used
    return result

print(solution())