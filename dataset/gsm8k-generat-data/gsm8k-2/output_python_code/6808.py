def solution():
    """Jerry works as an independent contractor for a company that pays him $40 per task. If each task takes him two hours to complete and he works 10 hours a day for a whole week, calculate the total amount of money he would earn at the end of the week."""
    tasks_per_hour = 0.5
    daily_tasks = tasks_per_hour * 10
    weekly_tasks = daily_tasks * 7
    weekly_earnings = weekly_tasks * 40
    result = weekly_earnings
    return result

print(solution())