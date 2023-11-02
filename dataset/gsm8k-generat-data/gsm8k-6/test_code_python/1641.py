def solution():
    # Calculate how many times John uses the bathroom during a 2.5-hour movie
    movie_length = 2.5 * 60  # convert movie length to minutes
    bathroom_frequency = movie_length // 50  # calculate how many times John uses the bathroom
    result = bathroom_frequency
    return result

print(solution())