def solution():
    # Calculate the water intake for one week
    water_per_week = 4 * 3 * 7

    # Calculate the water intake for the second week, accounting for the two missed doses
    water_in_missing_doses = 4 * 2
    water_per_second_week = 4 * 3 * 6 + water_in_missing_doses

    # Calculate the total water intake over the two weeks
    total_water_intake = water_per_week + water_per_second_week
    result = total_water_intake
    return result

print(solution())