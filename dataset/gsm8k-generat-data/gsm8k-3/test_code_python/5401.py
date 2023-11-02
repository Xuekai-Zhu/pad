def solution():
    """Lyka wants to buy a smartphone worth $160 but she only has $40 at the moment. She plans to save an equal amount of money per week for two months for the remaining amount that she needs. How much should she save per week?"""
    # Define the cost of the smartphone and the initial savings
    PHONE_COST = 160
    INITIAL_SAVINGS = 40

    # Calculate the remaining amount needed to buy the smartphone
    remaining_amount = PHONE_COST - INITIAL_SAVINGS

    # Calculate the number of weeks in two months
    WEEKS_IN_TWO_MONTHS = 8

    # Calculate the amount Lyka should save per week
    weekly_savings = remaining_amount / WEEKS_IN_TWO_MONTHS

    # Display the amount Lyka should save per week
    result = weekly_savings
    return result

print(solution())