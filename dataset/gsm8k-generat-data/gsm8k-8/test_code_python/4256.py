def solution():
    num_tasks_per_day = 100
    pay_per_task = 1.2
    num_days_per_week = 6

    # Calculate the total amount earned in a week
    total_earned = num_tasks_per_day * pay_per_task * num_days_per_week

    result = total_earned
    return result

print(solution())