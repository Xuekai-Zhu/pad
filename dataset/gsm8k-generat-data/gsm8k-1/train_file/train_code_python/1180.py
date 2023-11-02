def solution():
    """Mr Fletcher hired 2 men to dig a well in his compound. They worked for 10 hours on the first day, 8 hours on the second day and finished the job on the third day after working 15 hours. If Mr Fletcher paid each of them $10 per hour of work, calculate the total amount of money they received altogether?"""
    worker_pay = 10
    worker_1_hours = 10
    worker_2_hours = 8 + 15
    total_hours = worker_1_hours + worker_2_hours
    total_pay = total_hours * worker_pay * 2
    result = total_pay
    return result

print(solution())