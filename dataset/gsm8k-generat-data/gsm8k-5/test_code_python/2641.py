def solution():
    total_campers = 150  # Total number of campers for the past three weeks
    campers_two_weeks_ago = 40  # Number of campers two weeks ago
    campers_three_weeks_ago = campers_two_weeks_ago - 10  # Number of campers three weeks ago

    # Calculate the number of campers last week
    campers_last_week = total_campers - campers_two_weeks_ago - campers_three_weeks_ago
    result = campers_last_week
    return result

print(solution())