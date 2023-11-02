def solution():
    """A 750 ml bottle of spirits costs $30.00 and has 16 servings per bottle.  Most restaurants will charge $8.00 for one serving.  How much money does a restaurant make on a bottle of spirits?"""
    # Define the cost of one bottle of spirits and the number of servings per bottle
    BOTTLE_COST = 30
    SERVINGS_PER_BOTTLE = 16

    # Define the price charged by the restaurant for one serving
    SERVING_PRICE = 8

    # Calculate the cost per serving for the bottle of spirits
    cost_per_serving = BOTTLE_COST / SERVINGS_PER_BOTTLE

    # Calculate the profit the restaurant makes on one bottle of spirits
    profit_per_bottle = SERVING_PRICE - cost_per_serving

    # Display the profit made by the restaurant on one bottle of spirits
    result = profit_per_bottle
    return result

print(solution())