def solution():
    
    total_campers = 150
    campers_2_weeks_ago = 40
    campers_3_weeks_ago = campers_2_weeks_ago - 10
    campers_last_week = total_campers - campers_2_weeks_ago - campers_3_weeks_ago
    result = campers_last_week
    return result

print(solution())