def solution():
    # Define Tina's regular and overtime rates
    regular_rate = 18.00
    overtime_rate = regular_rate * 1.5

    # Calculate Tina's earnings for each day
    earnings_per_day = (8 * regular_rate) + (2 * overtime_rate)

    # Calculate Tina's earnings for the entire week
    total_weekly_earnings = earnings_per_day * 5

    result = total_weekly_earnings
    return result

print(solution())