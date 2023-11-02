def solution():
    """Alan went to the market and bought 20 eggs at the price of $2 per egg. He bought 6 chickens for the price of $8 per chicken. How much money did Alan spend at the market?"""
    # Define the cost of each egg and each chicken
    EGG_PRICE = 2
    CHICKEN_PRICE = 8

    # Define the number of eggs and chickens purchased
    eggs_quantity = 20
    chickens_quantity = 6

    # Calculate the total cost of the eggs
    eggs_cost = eggs_quantity * EGG_PRICE

    # Calculate the total cost of the chickens
    chickens_cost = chickens_quantity * CHICKEN_PRICE

    # Calculate the total cost of everything
    total_cost = eggs_cost + chickens_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())