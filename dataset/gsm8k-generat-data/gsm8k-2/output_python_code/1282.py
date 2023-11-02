def solution():
    """Dan spent an hour doing 400 work tasks at $0.25 each. Then Dan spent an hour doing 5 work tasks at $2.00 each. How much more did Dan make doing the good work compared to the lower-paid work?"""
    task1_pay = 0.25
    task1_count = 400
    task1_pay_total = task1_pay * task1_count
    task2_pay = 2.00
    task2_count = 5
    task2_pay_total = task2_pay * task2_count
    difference = task2_pay_total - task1_pay_total
    result = difference
    return result

print(solution())