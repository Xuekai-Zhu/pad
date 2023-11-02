def solution():
    """James decides to sell 80% of his toys. He bought them for $20 each and sells them for $30 each. If he had 200 toys how much more money did he have compared to before he bought them?"""
    initial_cost = 20
    sell_price = 30
    percent_to_sell = 80
    num_toys = 200
    num_sold = num_toys * (percent_to_sell / 100)
    total_profit = (num_sold * sell_price) - (num_toys * initial_cost)
    result = total_profit
    return result

print(solution())