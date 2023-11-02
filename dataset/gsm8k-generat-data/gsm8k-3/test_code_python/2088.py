def solution():
    """Sam is serving spaghetti and meatballs for dinner.  The pasta costs $1.00 per box, a jar of sauce is $2.00 and 1 pound of meatballs is $5.00.  He wants to stretch this meal into 8 servings.  How much does each serving cost?"""
    # Define the cost of each ingredient
    PASTA_COST = 1
    SAUCE_COST = 2
    MEATBALL_COST = 5

    # Define the amount of each ingredient needed for 8 servings
    pasta_boxes = 2
    sauce_jars = 1
    meatballs_pounds = 0.5

    # Calculate the total cost of the ingredients
    total_cost = pasta_boxes * PASTA_COST + sauce_jars * SAUCE_COST + meatballs_pounds * MEATBALL_COST

    # Calculate the cost per serving
    cost_per_serving = total_cost / 8

    # Display the cost per serving
    result = cost_per_serving
    return result

print(solution())