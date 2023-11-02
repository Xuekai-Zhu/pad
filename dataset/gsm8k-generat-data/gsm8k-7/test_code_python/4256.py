def solution():
    num_tasks = 100
    pay_per_task = 1.2
    num_days_per_week = 6

    # Calculate the total pay for one day
    total_pay_per_day = num_tasks * pay_per_task

    # Calculate the total pay for one week
    total_pay_per_week = total_pay_per_day * num_days_per_week

    result = total_pay_per_week
    return result

print(solution())