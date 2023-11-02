def solution():
    """Andy walks 50 meters from his house to school. After school, he comes back to the house and goes to the market. If he walks 140 meters in total, how many meters is the distance between the house and the market?"""
    # Calculate the total distance Andy walks from the house to school and back
    round_trip_distance = 50 * 2

    # Calculate the remaining distance Andy walks to get to the market
    market_distance = 140 - round_trip_distance

    # Return the result
    result = market_distance
    return result

print(solution())