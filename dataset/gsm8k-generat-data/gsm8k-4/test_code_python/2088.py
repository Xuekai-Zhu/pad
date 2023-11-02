def solution():
    """Sam is serving spaghetti and meatballs for dinner. The pasta costs $1.00 per box, a jar of sauce is $2.00 and 1 pound of meatballs is $5.00. He wants to stretch this meal into 8 servings. How much does each serving cost?"""
    # Define the cost of each ingredient
    pasta_cost = 1.00
    sauce_cost = 2.00
    meatball_cost = 5.00

    # Calculate the total cost of the meal
    total_cost = pasta_cost + sauce_cost + meatball_cost

    # Calculate the cost per serving
    cost_per_serving = total_cost / 8

    result = cost_per_serving
    return result

print(solution())