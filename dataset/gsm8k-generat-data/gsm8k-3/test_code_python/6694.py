def solution():
    """John has started at a job he works every day 10 days ago.  So far, he's made $250.  How many more days must John work before he makes twice this amount, assuming he makes the same amount every day?"""
    # Calculate John's daily earnings
    daily_earnings = 250 / 10

    # Calculate the total amount John needs to make
    total_amount = 250 * 2

    # Calculate the number of days John needs to work to reach this amount
    days_to_work = round(total_amount / daily_earnings) - 10

    # Display the number of days John needs to work
    result = days_to_work
    return result

print(solution())