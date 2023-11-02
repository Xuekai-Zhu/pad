def solution():
    # Calculate the number of campers three weeks ago
    campers_three_weeks_ago = (40-10)

    # Calculate the total number of campers for the past two weeks
    total_campers_last_two_weeks = 150 - campers_three_weeks_ago - 40

    # Calculate the number of campers last week
    campers_last_week = total_campers_last_two_weeks // 2

    result = campers_last_week
    return result

print(solution())