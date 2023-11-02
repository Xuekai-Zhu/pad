def solution():
    
    basic_cable_cost = 15
    movie_channel_cost = 12
    sports_channel_cost = movie_channel_cost - 3
    total_cost = basic_cable_cost + movie_channel_cost + sports_channel_cost
    result = total_cost
    return result

print(solution())