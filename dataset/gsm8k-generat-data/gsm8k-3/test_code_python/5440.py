def solution():
    """Each week Jaime saves $50. Every two weeks she spends $46 of her savings on a nice lunch with her mum. How long will it take her to save $135?"""
    # Define Jaime's weekly savings and biweekly spending
    WEEKLY_SAVINGS = 50
    BIWEEKLY_SPENDING = 46

    # Initialize Jaime's savings and the number of weeks passed
    savings = 0
    weeks = 0

    # Loop until Jaime has saved $135
    while savings < 135:
        # Add Jaime's weekly savings
        savings += WEEKLY_SAVINGS

        # Subtract Jaime's biweekly spending every other week
        if weeks % 2 == 1:
            savings -= BIWEEKLY_SPENDING

        # Increment the number of weeks passed
        weeks += 1

    # Display the number of weeks passed
    result = weeks
    return result

print(solution())