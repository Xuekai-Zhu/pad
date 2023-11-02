def solution():
    """An adult panda can eat 138 pounds of bamboo each day. A baby panda can eat 50 pounds of bamboo a day. How many pounds of bamboo will the pandas eat in a week?"""
    # Define the daily bamboo consumption of each panda
    ADULT_CONSUMPTION = 138
    BABY_CONSUMPTION = 50

    # Calculate the total weekly consumption of bamboo
    total_consumption = 7 * (ADULT_CONSUMPTION + BABY_CONSUMPTION)

    # Return the result
    result = total_consumption
    return result

print(solution())