def solution():
    bathroom_frequency = 50  # John uses the bathroom every 50 minutes
    movie_length = 2.5 * 60  # The movie is 2.5 hours long, converted to minutes

    # Calculate the number of times John uses the bathroom during the movie
    bathroom_count = movie_length // bathroom_frequency

    result = bathroom_count
    return result

print(solution())