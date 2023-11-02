def solution():
    # Calculate the total cost of their meal before the tip
    total_cost = 9 + (2 * 20) + 11

    # Calculate the amount of the tip
    tip_amount = 0.3 * total_cost

    # Calculate the total cost of the meal including the tip
    total_cost_with_tip = total_cost + tip_amount

    result = total_cost_with_tip
    return result

print(solution())