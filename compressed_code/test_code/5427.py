def solution():
    
    buy_price = 40
    sell_price = 60
    num_rugs = 20
    revenue = sell_price * num_rugs
    cost = buy_price * num_rugs
    profit = revenue - cost
    result = profit
    return result

print(solution())