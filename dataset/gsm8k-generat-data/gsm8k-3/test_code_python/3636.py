def solution():
    """Janet wanted to move out of her parents' house and rent her own apartment.  She had $2,225 saved.  She found an apartment that cost $1,250 per month that was perfect for her.  The landlord said that she needed to be able to pay 2 months' rent in advance to rent the place and she would also need to put down a deposit of $500.  How much more money did Janet need in order to rent the apartment?"""
    # Define the cost of rent per month and the amount of money Janet has saved
    RENT_PER_MONTH = 1250
    MONEY_SAVED = 2225

    # Define the required upfront payment
    UPFRONT_PAYMENT = 2 * RENT_PER_MONTH + 500

    # Calculate how much more money Janet needs to rent the apartment
    additional_money_needed = UPFRONT_PAYMENT - MONEY_SAVED

    # Display how much more money Janet needs to rent the apartment
    result = additional_money_needed
    return result

print(solution())