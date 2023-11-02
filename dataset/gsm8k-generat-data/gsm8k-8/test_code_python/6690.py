def solution():
    # Define the cost of flasks and calculate the remaining budget
    flask_cost = 150
    remaining_budget = 325 - flask_cost

    # Define the cost of test tubes and calculate the remaining budget
    test_tube_cost = 2/3 * flask_cost
    remaining_budget -= test_tube_cost

    # Define the cost of safety gear and calculate the remaining budget
    safety_gear_cost = 1/2 * test_tube_cost
    remaining_budget -= safety_gear_cost

    result = remaining_budget
    return result

print(solution())