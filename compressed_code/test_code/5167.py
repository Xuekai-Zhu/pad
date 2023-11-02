def solution():
    
    total_budget = 325
    flask_cost = 150
    test_tube_cost = (2/3) * flask_cost
    safety_gear_cost = 0.5 * test_tube_cost
    total_spent = flask_cost + test_tube_cost + safety_gear_cost
    remaining_budget = total_budget - total_spent
    result = remaining_budget
    return result

print(solution())