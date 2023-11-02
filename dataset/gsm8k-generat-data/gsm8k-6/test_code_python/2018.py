def solution():
    # Calculate the cost of adding the movie channels
    movie_channels = 12
    # Calculate the cost of adding the sports channels
    sports_channels = movie_channels - 3
    # Calculate the total cost of adding both movie and sports channels
    total_channels = 15 + movie_channels + sports_channels
    result = total_channels
    return result

print(solution())