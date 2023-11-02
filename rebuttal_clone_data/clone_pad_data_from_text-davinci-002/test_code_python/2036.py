def solution():
    total_days = 30
    days_passed = 4/5
    pills_left = 12
    pills_per_day = (total_days - days_passed) / pills_left
    result = pills_per_day
    
    return result

print(solution())