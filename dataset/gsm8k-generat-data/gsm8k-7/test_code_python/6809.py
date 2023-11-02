def solution():
    pay_per_task = 40
    hours_per_task = 2
    daily_hours = 10
    days_in_week = 7

    # Calculate the total number of tasks Jerry completes in a week
    total_tasks = daily_hours * days_in_week / hours_per_task

    # Calculate the total amount of money Jerry earns in a week
    total_pay = total_tasks * pay_per_task
    result = total_pay
    return result

print(solution())