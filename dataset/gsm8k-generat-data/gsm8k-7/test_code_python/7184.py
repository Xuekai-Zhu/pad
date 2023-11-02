def solution():
    selling_price = 30
    num_pairs = 10
    profit_per_pair = (selling_price / 2) - 20  # half the selling price minus the cost of the sign
    total_profit = profit_per_pair * num_pairs
    cost_of_sunglasses = (total_profit / 2) / num_pairs
    result = cost_of_sunglasses
    return result

print(solution())