def solution():
    """Jessica has a basic cable television service for $15 per month. If she adds the movie channels, it will cost an additional $12 per month. The sports channels cost $3 less per month than the movie channels. If Jessica adds the movie channels and the sports channels, what will her total monthly payment be?"""
    basic_service = 15
    movie_channels = 12
    sports_channels = movie_channels - 3
    total_cost = basic_service + movie_channels + sports_channels
    result = total_cost
    return result

print(solution())