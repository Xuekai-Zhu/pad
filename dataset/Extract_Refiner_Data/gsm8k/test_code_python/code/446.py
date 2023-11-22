def solution():
    
    # Define the prices of the super ticket and popcorn and soda
    SUPER_TICKET_PRICE = 20
    POPCORN_SODA_PRICE = 1

    # Define the prices of the popcorn and soda
    POPCORN_PRICE = 12 - SUPER_TICKET_PRICE - POPCORN_SODA_PRICE

    # Define the savings from the soda
    SODA_SAVINGS = 2

    # Calculate the regular price of popcorn
    REGULAR_PRICE = POPCORN_PRICE + SODA_SAVINGS

    # Display the regular price of popcorn
    result = REGULAR_PRICE
    return result

print(solution())