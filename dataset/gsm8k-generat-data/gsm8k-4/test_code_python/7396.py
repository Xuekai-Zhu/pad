def solution():
    """A 750 ml bottle of spirits costs $30.00 and has 16 servings per bottle. Most restaurants will charge $8.00 for one serving. How much money does a restaurant make on a bottle of spirits?"""
    # Define the cost and number of servings per bottle
    cost_per_bottle = 30.00
    servings_per_bottle = 16

    # Define the price per serving
    price_per_serving = 8.00

    # Calculate the revenue per bottle and the profit per bottle
    revenue_per_bottle = servings_per_bottle * price_per_serving
    profit_per_bottle = revenue_per_bottle - cost_per_bottle

    # Return the profit per bottle
    result = profit_per_bottle
    return result

print(solution())