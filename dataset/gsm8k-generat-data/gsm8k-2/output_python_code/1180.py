def solution():
    """Mr Fletcher hired 2 men to dig a well in his compound. They worked for 10 hours on the first day, 8 hours on the second day and finished the job on the third day after working 15 hours. If Mr Fletcher paid each of them $10 per hour of work, calculate the total amount of money they received altogether?"""
    hours_day1 = 10
    hours_day2 = 8
    hours_day3 = 15
    pay_rate = 10
    total_hours = hours_day1 + hours_day2 + hours_day3
    total_pay = total_hours * pay_rate * 2  # 2 workers
    result = total_pay
    return result

print(solution())