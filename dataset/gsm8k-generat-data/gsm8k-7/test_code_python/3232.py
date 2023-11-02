def solution():
    original_price = 100000
    profit = 0.1
    after_profit_price = original_price * (1 + profit)
    loss = 0.1
    final_price = after_profit_price * (1 - loss)
    result = final_price
    return result

print(solution())