def solution():
    # Calculate the total earnings for each job
    earnings_job1 = 3 * 7  # $7 per hour, 3 hours worked
    earnings_job2 = 2 * 10  # $10 per hour, 2 hours worked
    earnings_job3 = 4 * 12  # $12 per hour, 4 hours worked

    # Calculate the total earnings for each day
    total_earnings_per_day = earnings_job1 + earnings_job2 + earnings_job3

    # Calculate the total earnings for 5 days
    total_earnings = total_earnings_per_day * 5

    result = total_earnings
    return result

print(solution())