def solution():
    # Define the cost per battery charge and the budget for battery charging
    cost_per_charge = 3.5
    budget = 20

    # Calculate the total cost of all four battery charges
    total_cost = cost_per_charge * 4

    # Calculate the remaining budget after paying for battery charges
    remaining_budget = budget - total_cost
    result = remaining_budget
    return result

print(solution())