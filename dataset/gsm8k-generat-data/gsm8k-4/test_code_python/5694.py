def solution():
    """Tim decides to do a movie marathon. The first movie is 2 hours long. The next movie is 50% longer. And the last movie is 1 hour shorter than the combined time of the previous 2 movies. How long was his movie marathon?"""
    # Define the length of the first movie
    movie1 = 2

    # Define the length of the second movie
    movie2 = movie1 * 1.5

    # Define the length of the third movie
    movie3 = movie1 + movie2 - 1

    # Calculate the total length of the movie marathon
    total_length = movie1 + movie2 + movie3

    result = total_length
    return result

print(solution())