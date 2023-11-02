def solution():
    
    hourly_wage = 10
    monday_hours = 7
    monday_tips = 18
    tuesday_hours = 5
    tuesday_tips = 12
    wednesday_hours = 7
    wednesday_tips = 20
    total_hours = monday_hours + tuesday_hours + wednesday_hours
    total_tips = monday_tips + tuesday_tips + wednesday_tips
    total_pay = (total_hours * hourly_wage) + total_tips
    result = total_pay
    return result

print(solution())