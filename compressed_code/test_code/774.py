def solution():
    
    monday_hours = 10
    tuesday_hours = 8
    remaining_hours = 20
    total_hours = monday_hours + tuesday_hours + remaining_hours
    hourly_rate = 20
    total_pay = total_hours * hourly_rate
    result = total_pay
    return result

print(solution())