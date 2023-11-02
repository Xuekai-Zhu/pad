def solution():
    """One-half of a pound of mangoes costs $0.60. How many pounds can Kelly buy with $12?"""
    # Define the cost and amount of mangoes
    COST_HALF_POUND = 0.60
    AMOUNT_HALF_POUND = 0.5

    # Calculate the cost per pound
    COST_PER_POUND = COST_HALF_POUND / AMOUNT_HALF_POUND

    # Calculate the amount of pounds Kelly can buy with $12
    amount = 12 / COST_PER_POUND

    # Display the amount of pounds Kelly can buy
    result = amount
    return result

print(solution())