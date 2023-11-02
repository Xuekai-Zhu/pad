def solution():
    """Janice gets paid $10 an hour for the first 40 hours she works each week, and $15 each hour of overtime after that. If Janice works 60 hours one week, how much money does she make?"""
    hourly_wage = 10
    overtime_wage = 15
    regular_hours = 40
    overtime_hours = 60 - regular_hours
    regular_pay = regular_hours * hourly_wage
    overtime_pay = overtime_hours * overtime_wage
    total_pay = regular_pay + overtime_pay
    result = total_pay
    
    return result

print(solution())