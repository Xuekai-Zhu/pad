def solution():
    # Calculate John's daily earnings
    daily_earnings = 250 / 10  # John has worked for 10 days so far

    # Calculate the total earnings required for John to make twice as much as he has made so far
    target_earnings = 250 * 2  

    # Calculate the number of days John needs to work to reach the target earnings
    days_to_work = (target_earnings - 250) / daily_earnings

    result = days_to_work
    return result

print(solution())