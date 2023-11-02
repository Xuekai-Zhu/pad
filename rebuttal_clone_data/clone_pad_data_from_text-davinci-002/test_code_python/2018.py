def solution():
    basic_cable = 15
    movie_channels = 12
    sports_channels = movie_channels - 3
    total_channels = basic_cable + movie_channels + sports_channels
    result = total_channels
    return result

print(solution())