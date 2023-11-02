def solution():
    """Jen buys and sells candy bars. She buys candy bars for 80 cents each and sells them for a dollar each. If she buys 50 candy bars and sells 48 of them, how much profit does she make in cents?"""
    buy_price = 80
    sell_price = 100
    num_bought = 50
    num_sold = 48
    profit_per_candy_bar = sell_price - buy_price
    total_profit = profit_per_candy_bar * num_sold
    result = total_profit
    return result

print(solution())