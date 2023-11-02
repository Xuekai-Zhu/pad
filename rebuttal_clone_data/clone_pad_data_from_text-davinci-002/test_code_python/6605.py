def solution():
    total_hours = 1500
    backstroke_hours = 50
    breaststroke_hours = 9
    butterfly_hours = 121
    freestyle_hours = 220
    sidestroke_hours = 220
    hours_completed = backstroke_hours + breaststroke_hours + butterfly_hours
    hours_needed = total_hours - hours_completed
    hours_per_month = freestyle_hours + sidestroke_hours
    months_needed = hours_needed / hours_per_month
    result = months_needed
    
    return result

print(solution())