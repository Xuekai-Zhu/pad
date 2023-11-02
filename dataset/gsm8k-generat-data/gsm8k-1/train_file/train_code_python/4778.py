def solution():
    """Melony makes $21 of profit every time she sells 3 shirts and four times as much profit when she sells two pairs of sandals. How much profit will she make if she sells 7 shirts and 3 pairs of sandals?"""
    shirts_sold = 7
    sandals_sold = 3
    profit_per_shirt = 21 / 3
    profit_per_sandal = profit_per_shirt * 4 / 2
    total_profit = (shirts_sold * profit_per_shirt) + (sandals_sold * profit_per_sandal)
    result = total_profit
    return result

print(solution())