def solution():
    # Calculate last week's earnings
    last_week_earnings = 35 * 10  # 35 hours at $10 per hour

    # Calculate this week's earnings
    this_week_earnings = 40 * 10.5  # 40 hours at $10.5 per hour (an increase of $0.5 per hour)

    # Calculate total earnings for two weeks
    total_earnings = last_week_earnings + this_week_earnings

    result = total_earnings
    return result

print(solution())