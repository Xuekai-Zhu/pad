def solution():
    """John uses the bathroom every 50 minutes.  How many times does he use the bathroom during a 2.5-hour movie?"""
    # Define the time of the movie in minutes
    movie_time = 2.5 * 60

    # Calculate the number of bathroom breaks
    breaks = movie_time // 50

    # return the result
    result = breaks
    return result

print(solution())