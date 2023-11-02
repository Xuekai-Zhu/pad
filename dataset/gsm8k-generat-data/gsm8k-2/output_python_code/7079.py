def solution():
    """Hallie is working as a waitress for $10/hour. On Monday, she works for 7 hours, and she receives $18 in tips. On Tuesday she works for 5 hours, and she receives $12 in tips. On Wednesday she works for 7 hours, and she receives $20 in tips. How much money does she earn in total from Monday to Wednesday?"""
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