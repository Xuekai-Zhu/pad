def solution():
    """Greg drives 30 miles from his workplace to the farmer's market. After buying his groceries at the farmers market, he drives home. To get home, he travels for 30 minutes at 20 miles per hour. How many miles in total does Greg travel?"""
    distance_to_market = 30
    time_to_get_home = 0.5
    speed_to_get_home = 20
    distance_to_home = speed_to_get_home * time_to_get_home
    total_distance = distance_to_market + distance_to_home
    result = total_distance
    return result

print(solution())