def solution():
    visits_per_month = 30000  # John's website gets 30000 visits per month
    earnings_per_visit = 0.01  # John earns $0.01 per visit

    # Calculate John's total earnings per month
    total_earnings = visits_per_month * earnings_per_visit

    # Calculate John's earnings per day
    earnings_per_day = total_earnings / 30  # Assuming a normal 30-day month

    result = earnings_per_day
    return result

print(solution())