def solution():
    """Tim does 100 tasks a day. They each pay $1.2. If he works 6 days a week how much does he make a week?"""
    # Define the number of tasks Tim does per day and the pay per task
    tasks_per_day = 100
    pay_per_task = 1.2

    # Calculate Tim's earnings per day
    earnings_per_day = tasks_per_day * pay_per_task

    # Calculate Tim's earnings per week
    earnings_per_week = earnings_per_day * 6

    # Display Tim's earnings per week
    result = earnings_per_week
    return result

print(solution())