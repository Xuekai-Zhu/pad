def solution():
    num_stockings = 5 * 5 + 4
    stocking_price = 20 * 0.9  # 10% discount
    monogramming_price = 5
    total_cost = num_stockings * (stocking_price + monogramming_price)
    result = total_cost
    return result

print(solution())