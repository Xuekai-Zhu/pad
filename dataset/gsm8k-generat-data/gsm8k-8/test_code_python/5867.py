def solution():
    # Calculate the total cost of the first three items
    total_cost = 2 * 18.5 + 63

    # Calculate the remaining budget
    remaining_budget = 260 - total_cost

    # Calculate the cost per item if split evenly
    cost_per_item = remaining_budget / 4
    result = cost_per_item
    return result

print(solution())