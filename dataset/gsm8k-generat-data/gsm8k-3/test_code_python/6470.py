def solution():
    """Greg drives 30 miles from his workplace to the farmer's market. After buying his groceries at the farmers market, he drives home. To get home, he travels for 30 minutes at 20 miles per hour. How many miles in total does Greg travel?"""
    # Define the distance from Greg's workplace to the farmer's market
    DISTANCE_1 = 30

    # Define the speed at which Greg drives to get home
    SPEED_2 = 20

    # Calculate the distance Greg travels to get home
    distance_2 = SPEED_2 * (30/60) # Convert 30 minutes to 0.5 hours

    # Calculate the total distance Greg travels
    total_distance = DISTANCE_1 + distance_2

    # Display the total distance
    result = total_distance
    return result

print(solution())