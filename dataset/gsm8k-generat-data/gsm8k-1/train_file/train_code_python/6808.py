def solution():
    """
    Jerry works as an independent contractor for a company that pays him $40 per task.
    If each task takes him two hours to complete and he works 10 hours a day for a whole week,
    calculate the total amount of money he would earn at the end of the week.
    """
    tasks_per_hour = 0.5  # It takes Jerry 2 hours to complete 1 task, so he completes 0.5 tasks per hour.
    hours_per_day = 10
    days_per_week = 7
    pay_per_task = 40
    tasks_per_day = tasks_per_hour * hours_per_day
    total_tasks = tasks_per_day * days_per_week
    total_pay = total_tasks * pay_per_task
    result = total_pay
    return result

print(solution())