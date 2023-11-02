def solution():
    """Robert and Teddy are planning to buy snacks for their friends.  Robert orders five boxes of pizza at $10 each box and ten cans of soft drinks at $2 each. Teddy buys six hamburgers at $3 each and an additional ten cans of soft drinks. How much do they spend in all?"""
    # Define the prices of each item
    PIZZA_PRICE = 10
    DRINK_PRICE = 2
    HAMBURGER_PRICE = 3

    # Calculate Robert's total cost
    robert_cost = 5 * PIZZA_PRICE + 10 * DRINK_PRICE

    # Calculate Teddy's total cost
    teddy_cost = 6 * HAMBURGER_PRICE + 10 * DRINK_PRICE

    # Calculate the total cost of all the snacks
    total_cost = robert_cost + teddy_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())