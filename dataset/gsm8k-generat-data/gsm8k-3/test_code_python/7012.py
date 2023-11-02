def solution():
    """Jake earns thrice what Jacob does. If Jacob earns $6 per hour, how much does Jake earn in 5 days working 8 hours a day?"""
    # Define Jacob's hourly rate
    JACOB_RATE = 6

    # Calculate Jake's hourly rate
    JAKE_RATE = 3 * JACOB_RATE

    # Calculate Jacob's total earnings in 5 days
    JACOB_EARNINGS = 5 * 8 * JACOB_RATE

    # Calculate Jake's total earnings in 5 days
    JAKE_EARNINGS = 5 * 8 * JAKE_RATE

    # Display Jake's total earnings
    result = JAKE_EARNINGS
    return result

print(solution())