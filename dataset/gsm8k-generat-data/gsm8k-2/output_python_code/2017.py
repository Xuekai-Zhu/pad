def solution():
    """Jessica has a basic cable television service for $15 per month. If she adds the movie channels, it will cost an additional $12 per month. The sports channels cost $3 less per month than the movie channels. If Jessica adds the movie channels and the sports channels, what will her total monthly payment be?"""
    basic_cable_cost = 15
    movie_channel_cost = 12
    sports_channel_cost = movie_channel_cost - 3
    total_cost = basic_cable_cost + movie_channel_cost + sports_channel_cost
    result = total_cost
    return result

print(solution())