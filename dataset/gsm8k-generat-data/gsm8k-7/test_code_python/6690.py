def solution():
    total_budget = 325
    flask_cost = 150
    test_tube_cost = (2/3) * flask_cost
    safety_gear_cost = (1/2) * test_tube_cost

    # Calculate the total cost of all items
    total_cost = flask_cost + test_tube_cost + safety_gear_cost

    # Calculate the remaining budget
    remaining_budget = total_budget - total_cost
    result = remaining_budget
    return result

print(solution())