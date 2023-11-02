def solution():
    # Calculate the total time the duck spends flying to the south and north
    south_time = 40
    north_time = 2 * south_time

    # Calculate the total time the duck spends traveling to the East
    east_time = 60

    # Calculate the total time the duck spends flying during all seasons
    total_time = south_time + north_time + east_time
    result = total_time
    return result

print(solution())