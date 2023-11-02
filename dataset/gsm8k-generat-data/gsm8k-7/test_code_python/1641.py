def solution():
    bathroom_interval = 50  # in minutes
    movie_duration = 2.5 * 60  # in minutes

    # Calculate the number of times John uses the bathroom
    num_bathroom_breaks = movie_duration // bathroom_interval

    result = num_bathroom_breaks
    return result

print(solution())