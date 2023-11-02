def solution():
    # Convert 2.5 hours to minutes
    movie_length = 2.5 * 60

    # Calculate the number of times John uses the bathroom
    bathroom_freq = 50   # in minutes
    num_bathroom_breaks = movie_length // bathroom_freq

    result = num_bathroom_breaks
    return result

print(solution())