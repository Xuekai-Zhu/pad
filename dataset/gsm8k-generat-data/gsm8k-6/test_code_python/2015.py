def solution():
    # Calculate the new earnings per hour after the 5% raise
    new_earnings_per_hour = 40 + (40 * 0.05)

    # Calculate the new weekly earnings, assuming Mark works 8 hours a day for 5 days a week
    new_weekly_earnings = new_earnings_per_hour * 8 * 5

    # Calculate the new weekly bills, including the personal trainer
    new_weekly_bills = 600 + 100

    # Calculate the amount Mark has leftover after paying his bills
    leftover = new_weekly_earnings - new_weekly_bills

    result = leftover
    return result

print(solution())