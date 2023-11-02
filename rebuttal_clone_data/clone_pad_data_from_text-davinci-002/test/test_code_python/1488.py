def solution():
    total_campers = 150
    campers_two_weeks_ago = 40
    campers_three_weeks_ago = campers_two_weeks_ago - 10
    campers_last_week = total_campers - (campers_two_weeks_ago + campers_three_weeks_ago)
    result = campers_last_week
    return result

print(solution())