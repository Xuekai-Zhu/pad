def solution():
    """A beadshop earns a third of its profit on Monday, a quarter of its profit on Tuesday and the rest of its profit on Wednesday. The shop makes a total profit of $1,200. How much profit, in dollars, was made on Wednesday?"""
    total_profit = 1200
    mon_profit = total_profit / 3
    tue_profit = total_profit / 4
    wed_profit = total_profit - mon_profit - tue_profit
    result = wed_profit
    return result

print(solution())