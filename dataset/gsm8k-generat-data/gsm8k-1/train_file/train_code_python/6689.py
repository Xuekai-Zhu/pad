def solution():
    """A laboratory needs flasks, test tubes, and safety gear to carry out its experiments. They were given a $325 budget for the month. They bought $150 worth of flasks, spent two-thirds of that amount on test tubes, and used half of the test tube cost on safety gear. How many dollars of their budget remained?"""
    budget = 325
    flask_cost = 150
    test_tube_cost = 2/3 * flask_cost
    safety_gear_cost = 1/2 * test_tube_cost
    total_cost = flask_cost + test_tube_cost + safety_gear_cost
    remaining_budget = budget - total_cost
    result = remaining_budget
    return result

print(solution())