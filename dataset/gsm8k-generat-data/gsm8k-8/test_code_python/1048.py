def solution():
    # Calculate the total amount of water used by the first three neighborhoods
    total_water_used = 150 + 2 * 150 + (2 * 150 + 100)

    # Calculate the amount of water left for the fourth neighborhood
    water_left = 1200 - total_water_used

    result = water_left
    return result

print(solution())