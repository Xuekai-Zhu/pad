def solution():
    """Grace is filling her pool in the backyard with a hose that sprays 50 gallons/hour. She waited for 3 hours but the pool wasn't full, so she decides to add another hose that sprays 70 gallons/hour, and after 2 more hours the pool is full. How much water can Grace’s pool contain?"""
    # Define the sprayer rates of the first and second hose
    sprayer_rate_1 = 50
    sprayer_rate_2 = 70

    # Define the time it took for the first hose to fill the pool
    time_1 = 3

    # Define the time it took for the second hose to fill the remaining pool
    time_2 = 2

    # Calculate the amount of water filled by the first hose
    water_1 = sprayer_rate_1 * time_1

    # Calculate the amount of water filled by the second hose
    water_2 = (sprayer_rate_1 + sprayer_rate_2) * time_2

    # Calculate the total amount of water in the pool
    total_water = water_1 + water_2

    result = total_water
    return result

print(solution())