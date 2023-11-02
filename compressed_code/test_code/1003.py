def solution():
    
    total_hours = 52
    monday_hours = 0.5 * 24
    tuesday_hours = 4
    wednesday_hours = 0.25 * 24
    thursday_hours = (monday_hours + tuesday_hours + wednesday_hours) / 2
    total_watched_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours
    friday_hours = total_hours - total_watched_hours
    result = friday_hours
    return result

print(solution())