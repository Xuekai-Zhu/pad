def solution():
    
    basic_service = 15
    movie_channels = 12
    sports_channels = movie_channels - 3
    total_cost = basic_service + movie_channels + sports_channels
    result = total_cost
    return result

print(solution())