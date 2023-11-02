def solution():
    """Greg drives 30 miles from his workplace to the farmer's market. After buying his groceries at the farmers market, he drives home. To get home, he travels for 30 minutes at 20 miles per hour. How many miles in total does Greg travel?"""
    # Define the distance to the farmer's market
    to_market_distance = 30

    # Define the time it takes to travel home and the speed at which Greg drives
    time_to_home = 0.5  # 30 minutes is 0.5 hours
    home_speed = 20

    # Calculate the distance traveled on the way home
    distance_to_home = time_to_home * home_speed

    # Calculate the total distance traveled
    total_distance = to_market_distance + distance_to_home

    # Return the result
    result = total_distance
    return result

print(solution())