def solution():
    
    full_battery_life = 60
    used_battery_life = full_battery_life * (3/4)
    exam_duration = 2
    remaining_battery_life = full_battery_life - used_battery_life - exam_duration
    result = remaining_battery_life
    return result

print(solution())