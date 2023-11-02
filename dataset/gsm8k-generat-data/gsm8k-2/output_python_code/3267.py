def solution():
    """Romeo buys five bars of chocolate at $5 each and sells these chocolates for a total of $90.
    If he uses packaging material that costs him $2 for each bar of chocolate, how much profit
    does he make for all the chocolates he sells?"""
    num_bars = 5
    buy_price = 5
    sell_price = 90 / num_bars
    packaging_cost = 2 * num_bars
    total_profit = (sell_price - buy_price) * num_bars - packaging_cost
    result = total_profit
    return result

print(solution())