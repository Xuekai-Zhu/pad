def solution():
    budget = 325
    flask_cost = 150
    test_tube_cost = flask_cost * 2/3
    safety_gear_cost = test_tube_cost * 1/2
    total_cost = flask_cost + test_tube_cost + safety_gear_cost
    remaining_budget = budget - total_cost
    result = remaining_budget
    return result

print(solution())