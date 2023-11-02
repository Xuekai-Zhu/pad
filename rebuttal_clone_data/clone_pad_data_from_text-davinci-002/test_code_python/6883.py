def solution():
    initial_cost = 100
    trade_in_value = 2
    purchase_price = 10
    total_cost = (initial_cost - (trade_in_value * initial_cost)) + (purchase_price * initial_cost)
    result = total_cost
    return result

print(solution())