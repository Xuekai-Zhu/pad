def solution():
    # Calculate his weekly earnings without overtime
    weekly_earnings = 8 * 5

    # Calculate his overtime earnings
    overtime_earnings = 8 * 1.5

    # Calculate his total earnings per week with overtime
    total_earnings = weekly_earnings + overtime_earnings

    # Calculate his monthly earnings with overtime
    monthly_earnings = total_earnings * 4
    result = monthly_earnings
    return result

print(solution())