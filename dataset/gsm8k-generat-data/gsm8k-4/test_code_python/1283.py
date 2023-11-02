def solution():
    """Dan spent an hour doing 400 work tasks at $0.25 each. Then Dan spent an hour doing 5 work tasks at $2.00 each. How much more did Dan make doing the good work compared to the lower-paid work?"""
    # Calculate the total earnings from the 400 tasks
    tasks_earnings = 400 * 0.25

    # Calculate the total earnings from the 5 tasks
    good_tasks_earnings = 5 * 2

    # Calculate the difference in earnings
    earnings_difference = good_tasks_earnings - tasks_earnings

    result = earnings_difference
    return result

print(solution())