def solution():
    """Mrs. Brynlee reduced the prices of items in her store by 20% after the local government gave small businesses in her county a subsidy. If the price of a shirt in the store was $60 and that of the leather jacket was $90, calculate the amount of money Teagan will pay for buying 5 shirts and 10 leather jackets at the reduced prices."""
    # Define the prices of the shirts and the leather jackets
    SHIRT_PRICE = 60
    JACKET_PRICE = 90

    # Define the discount percentage
    DISCOUNT_PERCENTAGE = 0.2

    # Calculate the reduced prices of the items
    reduced_shirt_price = SHIRT_PRICE - (SHIRT_PRICE * DISCOUNT_PERCENTAGE)
    reduced_jacket_price = JACKET_PRICE - (JACKET_PRICE * DISCOUNT_PERCENTAGE)

    # Calculate the total cost of buying 5 shirts and 10 leather jackets at the reduced prices
    total_cost = (reduced_shirt_price * 5) + (reduced_jacket_price * 10)

    # Return the result
    result = total_cost
    return result

print(solution())