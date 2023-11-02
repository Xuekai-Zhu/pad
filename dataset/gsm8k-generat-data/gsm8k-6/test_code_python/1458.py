def solution():
    # Calculate the total cost of the meal
    total_cost = 10 + 4*20  # $10 for the appetizer and $20 for each entree
    tip = 0.20 * total_cost  # 20% tip
    total_amount = total_cost + tip
    result = total_amount
    return result

print(solution())