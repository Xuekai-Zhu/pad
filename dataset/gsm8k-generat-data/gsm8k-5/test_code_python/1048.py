def solution():
    total_water = 1200  # The water tower holds 1200 barrels of water
    neighborhood1 = 150  # The first neighborhood uses 150 barrels of water in a week
    neighborhood2 = 2 * neighborhood1  # The second neighborhood uses twice as many barrels of water as the first neighborhood
    neighborhood3 = neighborhood2 + 100  # The third neighborhood uses one hundred more barrels of water than the second neighborhood
    water_used = neighborhood1 + neighborhood2 + neighborhood3  # Total water used by the first three neighborhoods

    # Calculate the amount of water left for the fourth neighborhood
    water_left = total_water - water_used
    result = water_left
    return result

print(solution())