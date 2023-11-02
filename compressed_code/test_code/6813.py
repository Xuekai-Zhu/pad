def solution():
    
    total_hours = 52
    monday_hours = 0.5 * 24
    tuesday_hours = 4
    wednesday_hours = 0.25 * 24
    previous_hours = monday_hours + tuesday_hours + wednesday_hours
    thursday_hours = previous_hours / 2
    hours_watched = previous_hours + thursday_hours
    friday_hours = total_hours - hours_watched
    result = friday_hours
    return result

print(solution())