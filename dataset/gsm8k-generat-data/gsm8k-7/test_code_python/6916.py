def solution():
    marked_price = 50
    cost_price = marked_price / 1.3 # cost price is 70% of marked price
    sale_price = cost_price * 0.9 # 10% discount during sale
    profit = sale_price - cost_price
    percent_profit = (profit / cost_price) * 100
    result = percent_profit
    return result

print(solution())