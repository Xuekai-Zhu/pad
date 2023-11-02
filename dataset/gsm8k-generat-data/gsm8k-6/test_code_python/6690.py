def solution():
    budget = 325  # dollars

    # Calculate the amount spent on test tubes
    flasks_cost = 150
    test_tubes_cost = (2/3) * flasks_cost
    safety_gear_cost = (1/2) * test_tubes_cost
    total_spent = flasks_cost + test_tubes_cost + safety_gear_cost

    # Calculate the remaining budget
    remaining_budget = budget - total_spent
    result = remaining_budget
    return result

print(solution())