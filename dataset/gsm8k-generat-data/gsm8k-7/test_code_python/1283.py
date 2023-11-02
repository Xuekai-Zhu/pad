def solution():
    tasks_per_hour = 400
    task_pay_low = 0.25
    tasks_per_hour_high = 5
    task_pay_high = 2.0

    # Calculate how much Dan made from the lower-paid work
    pay_low = tasks_per_hour * task_pay_low

    # Calculate how much Dan made from the higher-paid work
    pay_high = tasks_per_hour_high * task_pay_high

    # Calculate the difference in pay
    pay_diff = pay_high - pay_low
    result = pay_diff
    return result

print(solution())