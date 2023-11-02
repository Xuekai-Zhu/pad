def solution():
    # Calculate Gervais' total distance
    gervais_total_distance = 315 * 3

    # Calculate Henri's daily distance
    henri_daily_distance = 1250 / 7

    # Calculate Henri's total distance
    henri_total_distance = henri_daily_distance * 7

    # Calculate the difference in distance
    distance_difference = henri_total_distance - gervais_total_distance
    result = distance_difference
    return result

print(solution())