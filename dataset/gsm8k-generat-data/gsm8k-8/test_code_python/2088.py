def solution():
    # Define the cost of each ingredient
    pasta_cost = 1
    sauce_cost = 2
    meatball_cost = 5

    # Calculate the total cost of the meal
    total_cost = pasta_cost + sauce_cost + meatball_cost

    # Divide the total cost by the number of servings
    cost_per_serving = total_cost / 8

    result = cost_per_serving
    return result

print(solution())