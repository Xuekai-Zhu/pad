def solution():
    """James is running a fundraiser selling candy bars. Each box has 10 candy bars in it. He sells 5 boxes. He sells each candy bar for $1.50 and buys each bar for $1. How much profit does he make from these sales?"""
    candy_bars_per_box = 10
    boxes_sold = 5
    selling_price = 1.5
    buying_price = 1
    total_candy_bars_sold = candy_bars_per_box * boxes_sold
    revenue = total_candy_bars_sold * selling_price
    cost = total_candy_bars_sold * buying_price
    profit = revenue - cost
    result = profit
    return result

print(solution())