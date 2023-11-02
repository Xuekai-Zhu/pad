def solution():
    cost_per_dozen = 50
    selling_price_per_half_dozen = 30
    num_of_dozen = 50

    cost_per_unit = cost_per_dozen / 12
    selling_price_per_unit = selling_price_per_half_dozen / 3

    profit_per_unit = selling_price_per_unit - cost_per_unit
    total_profit = profit_per_unit * num_of_dozen * 12

    result = total_profit
    return result

print(solution())