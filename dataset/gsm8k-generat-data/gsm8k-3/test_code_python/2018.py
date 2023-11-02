def solution():
    """Jessica has a basic cable television service for $15 per month. If she adds the movie channels, it will cost an additional $12 per month. The sports channels cost $3 less per month than the movie channels. If Jessica adds the movie channels and the sports channels, what will her total monthly payment be?"""
    # Define the cost of each service
    BASIC_SERVICE_COST = 15
    MOVIE_CHANNEL_COST = 12
    SPORTS_CHANNEL_COST = 9

    # Determine the total cost if Jessica adds both movie channels and sports channels
    total_cost = BASIC_SERVICE_COST + MOVIE_CHANNEL_COST + SPORTS_CHANNEL_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())