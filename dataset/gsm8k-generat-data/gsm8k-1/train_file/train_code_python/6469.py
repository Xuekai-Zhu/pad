def solution():
    """Greg drives 30 miles from his workplace to the farmer's market. After buying his groceries at the farmers market, he drives home. To get home, he travels for 30 minutes at 20 miles per hour. How many miles in total does Greg travel?"""
    distance_to_market = 30
    time_to_drive_home = 0.5  # 30 minutes = 0.5 hours
    speed_to_drive_home = 20
    distance_driven_home = time_to_drive_home * speed_to_drive_home
    total_distance = distance_to_market + distance_driven_home
    result = total_distance
    return result

print(solution())