def solution():
    buy_price = 40
    sell_price = 60
    num_rugs = 20

    # Calculate the total cost of buying all the rugs
    total_buy_cost = buy_price * num_rugs

    # Calculate the total revenue from selling all the rugs
    total_sell_revenue = sell_price * num_rugs

    # Calculate the profit from selling all the rugs
    total_profit = total_sell_revenue - total_buy_cost
    result = total_profit
    return result

print(solution())