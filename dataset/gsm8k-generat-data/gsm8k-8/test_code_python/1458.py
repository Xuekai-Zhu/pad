def solution():
    # Calculate the cost of the appetizer and entrees
    appetizer_cost = 10
    entrees_cost = 4 * 20

    # Calculate the total cost before tip
    total_cost_before_tip = appetizer_cost + entrees_cost

    # Calculate the tip amount
    tip_amount = 0.2 * total_cost_before_tip

    # Calculate the total cost with tip
    total_cost_with_tip = total_cost_before_tip + tip_amount

    result = total_cost_with_tip
    return result

print(solution())