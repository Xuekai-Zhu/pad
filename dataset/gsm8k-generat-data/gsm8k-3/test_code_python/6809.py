def solution():
    """Jerry works as an independent contractor for a company that pays him $40 per task. If each task takes him two hours to complete and he works 10 hours a day for a whole week, calculate the total amount of money he would earn at the end of the week."""
    # Define Jerry's pay per task and hours worked per day
    PAY_PER_TASK = 40
    HOURS_PER_DAY = 10

    # Calculate the number of tasks Jerry can complete in one day
    tasks_per_day = HOURS_PER_DAY / 2

    # Calculate the total number of tasks completed in a week
    total_tasks = tasks_per_day * 7

    # Calculate Jerry's total earnings for the week
    total_earnings = total_tasks * PAY_PER_TASK

    # Display Jerry's total earnings for the week
    result = total_earnings
    return result

print(solution())