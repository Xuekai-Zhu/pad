def solution():
    initial_mission_days = 5
    mission_time_increase = 60
    increased_mission_days = mission_time_increase / 100 * initial_mission_days + initial_mission_days
    second_mission_days = 3
    total_mission_days = increased_mission_days + second_mission_days
    
    result = total_mission_days
    
    return result

print(solution())