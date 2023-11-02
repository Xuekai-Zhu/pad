def solution():
    """Mike wants to buy a new phone. The cost of the phone is $1300. How much more money does Mike need if he already has 40% of the amount he needs?"""
    # Define the cost of the phone
    PHONE_COST = 1300

    # Define the percentage of the cost that Mike already has
    PERCENTAGE_OWNED = 0.4

    # Calculate how much money Mike still needs
    still_needs = PHONE_COST - (PHONE_COST * PERCENTAGE_OWNED)

    # Display how much more money Mike needs
    result = still_needs
    return result

print(solution())