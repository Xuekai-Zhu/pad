def solution():
    
    initial_cost = 20
    sell_price = 30
    percent_to_sell = 80
    num_toys = 200
    num_sold = num_toys * (percent_to_sell / 100)
    total_profit = (num_sold * sell_price) - (num_toys * initial_cost)
    result = total_profit
    return result

print(solution())