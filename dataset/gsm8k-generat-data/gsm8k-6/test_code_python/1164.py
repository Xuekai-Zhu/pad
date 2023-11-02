def solution():
    # Calculate the total amount of water that has leaked out of the tank in the first 4 hours
    leaked_water = 2 * 4  # the tank loses 2 gallons of water per hour

    # Calculate the total amount of water added to the tank in the first 4 hours
    added_water = 0 + 0 + 1 + 3  # 0 added in the first 2 hours, 1 added in hour 3, 3 added in hour 4

    # Calculate the total amount of water left in the tank at the end of the fourth hour
    remaining_water = 40 - leaked_water + added_water

    result = remaining_water
    return result

print(solution())