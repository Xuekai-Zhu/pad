def solution():
    """Janice gets paid $10 an hour for the first 40 hours she works each week, and $15 each hour of overtime after that. If Janice works 60 hours one week, how much money does she make?"""
    regular_hours = 40
    regular_rate = 10
    overtime_rate = 15
    overtime_hours = 20
    overtime_pay = overtime_hours * overtime_rate
    regular_pay = regular_hours * regular_rate
    total_pay = regular_pay + overtime_pay
    result = total_pay
    return result

print(solution())