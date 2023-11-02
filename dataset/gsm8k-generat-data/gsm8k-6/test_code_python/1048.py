def solution():
    # Calculate the total amount of water used by the first three neighborhoods
    total_water_used = 150 + 2*150 + 100 + 150  # first neighborhood uses 150 barrels, second uses twice as many, third uses 100 more than second

    # Calculate the amount of water left for the fourth neighborhood
    water_left = 1200 - total_water_used
    result = water_left
    return result

print(solution())