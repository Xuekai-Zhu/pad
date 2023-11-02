def solution():
    
    first_mission_days = 5
    first_mission_extra_days = 0.6 * first_mission_days
    total_first_mission_days = first_mission_days + first_mission_extra_days
    second_mission_days = 3
    total_mission_days = total_first_mission_days + second_mission_days
    result = total_mission_days
    return result

print(solution())