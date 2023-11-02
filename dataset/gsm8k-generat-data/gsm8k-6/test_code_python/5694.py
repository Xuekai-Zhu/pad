def solution():
    # Calculate the total length of the movie marathon
    movie1 = 2
    movie2 = 1.5 * movie1  # 50% longer than the first movie
    movie3 = (movie1 + movie2) - 1  # 1 hour shorter than the combined time of the first two movies
    total_length = movie1 + movie2 + movie3
    result = total_length
    return result

print(solution())