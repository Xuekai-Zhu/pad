def solution():
    hours_mon_wed_fri = 1
    hours_tue_thur = 0.5
    hours_sat = 2
    
    total_hours = (hours_mon_wed_fri * 3) + (hours_tue_thur * 2) + hours_sat
    
    result = total_hours
    return result

print(solution())