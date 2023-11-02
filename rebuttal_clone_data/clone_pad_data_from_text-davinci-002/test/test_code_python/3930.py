def solution():
    cost_per_bar = 80
    sale_price_per_bar = 100
    bars_bought = 50
    bars_sold = 48
    profit = (bars_sold * sale_price_per_bar) - (bars_bought * cost_per_bar)
    result = profit
    return result

print(solution())