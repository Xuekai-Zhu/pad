def solution():
    
    num_bars = 5
    buy_price = 5
    sell_price = 90 / num_bars
    packaging_cost = 2 * num_bars
    total_profit = (sell_price - buy_price) * num_bars - packaging_cost
    result = total_profit
    return result

print(solution())