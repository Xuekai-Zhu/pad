def solution():
    budget = 325  # The laboratory has $325 to spend
    flasks_cost = 150  # They spend $150 on flasks

    # Calculate the cost of test tubes and safety gear
    test_tubes_cost = (2/3) * flasks_cost
    safety_gear_cost = (1/2) * test_tubes_cost

    # Calculate the total cost of all items
    total_cost = flasks_cost + test_tubes_cost + safety_gear_cost

    # Calculate the remaining budget
    remaining_budget = budget - total_cost
    result = remaining_budget
    return result

print(solution())