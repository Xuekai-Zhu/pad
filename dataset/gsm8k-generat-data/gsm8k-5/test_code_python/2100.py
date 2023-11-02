def solution():
    cost_pizza = 12 * 2  # Victoria spent $12 each on 2 boxes of pizza
    cost_juice = 2 * 2  # Victoria spent $2 each on 2 packs of juice drinks
    total_cost = cost_pizza + cost_juice  # Calculate the total cost of the snacks

    # Calculate the amount of money Victoria should return to her mother
    return_money = 50 - total_cost
    result = return_money
    return result

print(solution())