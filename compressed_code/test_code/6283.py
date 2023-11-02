def solution():
    
    hourly_rate = 9
    monday_hours = 4
    wednesday_hours = 3
    friday_hours = 6
    total_hours = monday_hours + wednesday_hours + friday_hours
    total_earned = total_hours * hourly_rate
    result = total_earned
    return result

print(solution())