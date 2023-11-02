def solution():
    """Hannah wanted to make an apple pie that would serve 8 people.  She needed 2 pounds of apples that were on sale for $2.00 per pound. The pre-made pie crust cost $2.00.  The lemon cost $.50 and the butter cost $1.50.  How much did each serving of pie cost?"""
    # Define the cost of each ingredient
    APPLE_PRICE = 2.00
    PIE_CRUST_PRICE = 2.00
    LEMON_PRICE = 0.50
    BUTTER_PRICE = 1.50

    # Define the amount of each ingredient needed
    apple_pounds = 2
    pie_crust_count = 1
    lemon_count = 1
    butter_cubes = 1

    # Calculate the total cost of all the ingredients
    total_cost = apple_pounds * APPLE_PRICE + \
                 pie_crust_count * PIE_CRUST_PRICE + \
                 lemon_count * LEMON_PRICE + \
                 butter_cubes * BUTTER_PRICE

    # Calculate the cost per serving
    cost_per_serving = total_cost / 8

    # Display the cost per serving
    result = cost_per_serving
    return result

print(solution())