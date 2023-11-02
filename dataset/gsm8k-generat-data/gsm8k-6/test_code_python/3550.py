def solution():
    # Calculate Porter's regular weekly earnings
    regular_earnings_weekly = 8 * 5  # $8 per day and works 5 times a week

    # Calculate his overtime earnings for the extra day
    overtime_earnings = (8 * 1.5) + 8  # extra 50% on top of his daily rate and plus $8 for the day worked

    # Calculate his total weekly earnings with overtime
    total_earnings_weekly = regular_earnings_weekly + overtime_earnings

    # Calculate his total monthly earnings with overtime
    total_earnings_monthly = total_earnings_weekly * 4  # 4 weeks in a month

    result = total_earnings_monthly
    return result

print(solution())