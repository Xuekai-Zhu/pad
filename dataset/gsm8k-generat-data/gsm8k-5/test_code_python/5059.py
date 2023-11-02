def solution():
    num_toys = 200  # James has 200 toys
    buy_price = 20  # James bought each toy for $20
    sell_price = 30  # James sells each toy for $30
    sell_percentage = 0.8  # James wants to sell 80% of his toys

    # Calculate the amount of money James makes by selling 80% of his toys
    num_to_sell = int(num_toys * sell_percentage)  # Calculate the number of toys to sell
    total_buy_price = num_toys * buy_price  # Calculate how much James paid for all the toys
    total_sell_price = num_to_sell * sell_price  # Calculate how much James earns by selling the toys
    profit = total_sell_price - total_buy_price  # Calculate the profit James makes

    result = profit
    return result

print(solution())