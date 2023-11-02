def solution():
    """Dan spent an hour doing 400 work tasks at $0.25 each. Then Dan spent an hour doing 5 work tasks at $2.00 each. How much more did Dan make doing the good work compared to the lower-paid work?"""
    task_per_hour_low = 400
    pay_per_task_low = 0.25
    task_per_hour_good = 5
    pay_per_task_good = 2.00
    total_pay_low = task_per_hour_low * pay_per_task_low
    total_pay_good = task_per_hour_good * pay_per_task_good
    difference = total_pay_good - total_pay_low
    result = difference
    return result

print(solution())