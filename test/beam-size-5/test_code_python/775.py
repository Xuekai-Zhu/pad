def solution():
    
    driving_time = 6
    driving_speed = 50
    hiking_speed = (driving_time / 2) - 5
    total_distance = driving_time * driving_speed
    vacation_spot_distance = total_distance - hiking_speed
    result = vacation_spot_distance
    return result

print(solution())