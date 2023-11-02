def solution():
    """Gervais drove an average of 315 miles for 3 days. Henri drove a total of 1,250 miles over one week. How many miles farther did Henri drive?"""
    # Calculate Gervais' total distance
    gervais_distance = 315 * 3

    # Calculate Henri's average daily distance
    henri_daily_distance = 1250 / 7

    # Calculate Henri's total distance
    henri_distance = henri_daily_distance * 3

    # Calculate the difference in distance
    distance_diff = henri_distance - gervais_distance

    # Display the difference in distance
    result = distance_diff
    return result

print(solution())