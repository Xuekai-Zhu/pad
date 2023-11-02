def solution():
    """John uses the bathroom every 50 minutes. How many times does he use the bathroom during a 2.5-hour movie?"""
    movie_length = 2.5 * 60  # convert hours to minutes
    bathroom_time = 50
    num_bathroom_breaks = movie_length // bathroom_time
    result = num_bathroom_breaks
    return result

print(solution())