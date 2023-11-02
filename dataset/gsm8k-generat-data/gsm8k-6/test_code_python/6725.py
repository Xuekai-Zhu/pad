def solution():
    # Calculate Janice's regular earnings
    regular_earnings = 30 * 5  # $30 per day, 5 days a week

    # Calculate Janice's overtime earnings
    overtime_earnings = 15 * 2 * 3  # $15 more per overtime shift, 3 overtime shifts this week

    # Calculate Janice's total earnings for the week
    total_earnings = regular_earnings + overtime_earnings

    result = total_earnings
    return result

print(solution())