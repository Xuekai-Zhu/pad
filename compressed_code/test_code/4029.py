def solution():
    
    initial_speed = 80
    final_speed = initial_speed * 1.2
    total_weeks = 16
    speed_gain_per_week = (final_speed - initial_speed) / total_weeks
    result = speed_gain_per_week
    return result

print(solution())