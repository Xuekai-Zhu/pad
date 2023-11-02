def solution():
    """Janet wanted to move out of her parents' house and rent her own apartment. She had $2,225 saved. She found an apartment that cost $1,250 per month that was perfect for her. The landlord said that she needed to be able to pay 2 months' rent in advance to rent the place and she would also need to put down a deposit of $500. How much more money did Janet need in order to rent the apartment?"""
    # Define the cost of the apartment per month, the number of months' rent required in advance, and the deposit
    RENT_PER_MONTH = 1250
    MONTHS_RENT_REQUIRED_IN_ADVANCE = 2
    DEPOSIT = 500

    # Define the amount of money Janet has saved
    savings = 2225

    # Calculate the total amount of money required to rent the apartment
    total_cost = (RENT_PER_MONTH * MONTHS_RENT_REQUIRED_IN_ADVANCE) + DEPOSIT

    # Calculate the difference between Janet's savings and the total cost
    difference = total_cost - savings

    # Return the amount of money Janet still needs in order to rent the apartment
    result = difference
    return result

print(solution())