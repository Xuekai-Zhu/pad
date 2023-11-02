def solution():
    
    monday_hours = 10
    tuesday_hours = 8
    weekly_hours_left = 20
    hourly_rate = 20
    total_worked_hours = monday_hours + tuesday_hours + weekly_hours_left
    total_earned_money = total_worked_hours * hourly_rate
    result = total_earned_money
    return result

print(solution())