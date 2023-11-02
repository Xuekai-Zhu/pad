def solution():
    """A beadshop earns a third of its profit on Monday, a quarter of its profit on Tuesday and the rest of its profit on Wednesday. The shop makes a total profit of $1,200. How much profit, in dollars, was made on Wednesday?"""
    total_profit = 1200
    monday_profit = total_profit / 3
    tuesday_profit = total_profit / 4
    wednesday_profit = total_profit - monday_profit - tuesday_profit
    result = wednesday_profit
    return result

print(solution())