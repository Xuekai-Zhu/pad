def solution():
    """Tim does 100 tasks a day. They each pay $1.2. If he works 6 days a week how much does he make a week?"""
    # Define the number of tasks Tim does each day and the amount of money he earns per task
    tasks_per_day = 100
    earnings_per_task = 1.2

    # Calculate the total earnings per day and per week
    daily_earnings = tasks_per_day * earnings_per_task
    weekly_earnings = daily_earnings * 6

    # return the result
    result = weekly_earnings
    return result

print(solution())