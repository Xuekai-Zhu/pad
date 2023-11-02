def solution():
    
    buy_price = 80
    sell_price = 100
    num_bought = 50
    num_sold = 48
    total_buy_cost = num_bought * buy_price
    total_sell_income = num_sold * sell_price
    profit = total_sell_income - total_buy_cost
    result = profit
    return result

print(solution())