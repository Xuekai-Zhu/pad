def solution():
    
    # Define the prices and quantities of each item
    MILKSHAKE_PRICE = 5.5
    BURGER_PLATTER_PRICE = 11
    SODA_PRICE = 1.5
    MILKSHAKE_QUANTITY = 6
    BURGER_PLATTER_QUANTITY = 9
    SODA_QUANTITY = 20

    # Calculate the total earnings from each item
    milkshakes_earnings = MILKSHAKE_PRICE * MILKSHAKE_QUANTITY
    burger_platters_earnings = BURGER_PLATTER_PRICE * BURGER_PLATTER_QUANTITY
    sodas_earnings = SODA_PRICE * SODA_QUANTITY

    # Calculate the total earnings
    total_earnings = milkshakes_earnings + burger_platters_earnings + sodas_earnings

    # Display the total e

print(solution())