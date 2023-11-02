def solution():
    """Jerry works as an independent contractor for a company that pays him $40 per task. If each task takes him two hours to complete and he works 10 hours a day for a whole week, calculate the total amount of money he would earn at the end of the week."""
    # Define the payment per task and the number of hours worked per day
    payment_per_task = 40
    hours_per_day = 10

    # Calculate the number of tasks Jerry completes per day and per week
    tasks_per_day = hours_per_day / 2
    tasks_per_week = tasks_per_day * 7

    # Calculate the total amount of money Jerry earns at the end of the week
    total_earnings = tasks_per_week * payment_per_task

    # return the result
    result = total_earnings
    return result

print(solution())