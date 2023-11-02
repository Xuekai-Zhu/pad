def solution():
    initial_cost = 80000
    percent_profit = 20
    percent_commission = 5
    actual_profit = initial_cost * (percent_profit / 100)
    commission = initial_cost * (percent_commission / 100)
    sale_price = initial_cost + actual_profit + commission
    result = sale_price
    
    return result

print(solution())