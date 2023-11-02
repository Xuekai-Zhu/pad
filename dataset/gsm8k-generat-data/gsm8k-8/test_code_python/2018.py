def solution():
    basic_cable_cost = 15
    movie_channel_cost = 12
    sports_channel_cost = movie_channel_cost - 3

    total_monthly_cost = basic_cable_cost + movie_channel_cost + sports_channel_cost
    result = total_monthly_cost
    return result

print(solution())