def solution():
    """Jessica has a basic cable television service for $15 per month. If she adds the movie channels, it will cost an additional $12 per month. The sports channels cost $3 less per month than the movie channels. If Jessica adds the movie channels and the sports channels, what will her total monthly payment be?"""
    # Define the cost of the basic cable service
    basic_cost = 15

    # Define the cost of the movie channels
    movie_cost = 12

    # Define the cost of the sports channels as $3 less than the movie channels
    sports_cost = movie_cost - 3

    # Calculate the total cost of adding both the movie and sports channels
    total_cost = basic_cost + movie_cost + sports_cost

    # Return the result
    result = total_cost
    return result

print(solution())