def solution():
    num_toys = 200
    buy_price = 20
    sell_price = 30
    percent_to_sell = 0.8

    # Calculate the total cost of all the toys
    total_cost = num_toys * buy_price

    # Calculate the number of toys to sell
    num_to_sell = int(percent_to_sell * num_toys)

    # Calculate the total revenue from selling the toys
    total_revenue = num_to_sell * sell_price

    # Calculate the profit
    profit = total_revenue - total_cost

    result = profit
    return result

print(solution())