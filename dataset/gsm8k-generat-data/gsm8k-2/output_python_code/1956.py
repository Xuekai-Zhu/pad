def solution():
    """John buys 500 newspapers. Each newspaper sells for $2. He sells 80% of them. He buys them all for 75% less than the price at which he sells them. How much profit does he make?"""
    num_newspapers = 500
    sell_price = 2
    buy_price = 0.25 * sell_price
    percent_sold = 0.8
    num_sold = percent_sold * num_newspapers
    revenue = num_sold * sell_price
    cost = num_newspapers * buy_price
    profit = revenue - cost
    result = profit
    return result

print(solution())