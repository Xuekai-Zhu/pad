def solution():
    
    hourly_wage = 9
    monday_hours = 4
    wednesday_hours = 3
    friday_hours = 6
    total_hours = monday_hours + wednesday_hours + friday_hours
    weekly_earnings = total_hours * hourly_wage
    result = weekly_earnings
    return result

print(solution())