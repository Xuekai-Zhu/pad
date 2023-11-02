def solution():
    total_battery_life = 60
    percent_remaining = 0.25  # three quarters used up
    exam_time = 2
    
    # Calculate the remaining battery life in hours
    remaining_battery_life = total_battery_life * percent_remaining
    
    # Subtract the exam time from the remaining battery life
    remaining_battery_life -= exam_time
    
    result = remaining_battery_life
    return result

print(solution())