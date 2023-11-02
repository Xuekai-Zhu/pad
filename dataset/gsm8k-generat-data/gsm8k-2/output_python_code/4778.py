def solution():
    """Melony makes $21 of profit every time she sells 3 shirts and four times as much profit when she sells two pairs of sandals. How much profit will she make if she sells 7 shirts and 3 pairs of sandals?"""
    shirts_profit = 21 / 3
    sandals_profit = shirts_profit * 4 / 2
    total_shirts_profit = shirts_profit * 7
    total_sandals_profit = sandals_profit * 3
    total_profit = total_shirts_profit + total_sandals_profit
    result = total_profit
    return result

print(solution())