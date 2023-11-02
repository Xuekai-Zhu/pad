def solution():
    # Calculate the number of campers three weeks ago
    campers_3_weeks_ago = (40 - 10)

    # Calculate the number of campers two weeks ago
    campers_2_weeks_ago = 40

    # Calculate the total number of campers for the three weeks
    total_campers = 150

    # Calculate the number of campers last week
    campers_last_week = total_campers - campers_3_weeks_ago - campers_2_weeks_ago
    result = campers_last_week
    return result

print(solution())