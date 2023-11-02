def solution():
    """In a fundraiser car wash activity, the 5th graders raised $147 on Friday. On Saturday, they made $7 more than twice their Friday earnings. Their earnings on Sunday are $78 more than their earnings on Friday. How much did they earn in three days?"""
    # Define the earning on Friday and Saturday
    friday_earnings = 147
    saturday_earnings = 2 * friday_earnings + 7

    # Define the earning on Sunday
    sunday_earnings = friday_earnings + 78

    # Calculate the total earnings over three days
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings

    result = total_earnings
    return result

print(solution())