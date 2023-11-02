def solution():
    basic_service_cost = 15
    movie_channel_cost = 12
    sports_channel_cost = movie_channel_cost - 3

    # Calculate the cost of adding the movie channels
    total_cost_movie_channels = basic_service_cost + movie_channel_cost

    # Calculate the cost of adding the sports channels
    total_cost_sports_channels = total_cost_movie_channels + sports_channel_cost

    # Calculate the total monthly payment
    total_monthly_payment = total_cost_sports_channels
    result = total_monthly_payment
    return result

print(solution())