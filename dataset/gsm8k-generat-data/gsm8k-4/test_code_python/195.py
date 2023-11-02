def solution():
    """Mary bought 5 boxes of drinks at $6 each box and 10 boxes of pizzas at $14 each box for her pizza party. She paid $200 for all the items. How much change did she get back?"""
    # Define the prices of drinks and pizzas
    DRINK_PRICE = 6
    PIZZA_PRICE = 14

    # Define the number of drinks and pizzas bought
    NUM_DRINKS = 5
    NUM_PIZZAS = 10

    # Calculate the total cost of drinks and pizzas
    total_cost = (DRINK_PRICE * NUM_DRINKS) + (PIZZA_PRICE * NUM_PIZZAS)

    # Calculate the change Mary got back
    change = 200 - total_cost

    # Return the change
    result = change
    return result

print(solution())