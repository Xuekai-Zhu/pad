def solution():
    """Melony makes $21 of profit every time she sells 3 shirts and four times as much profit when she sells two pairs of sandals. How much profit will she make if she sells 7 shirts and 3 pairs of sandals?"""
    # Calculate the profit per 3 shirts
    shirts_profit = 21

    # Calculate the profit per 2 pairs of sandals
    sandals_profit = shirts_profit * 4

    # Calculate the profit from selling 7 shirts
    shirts_profit_total = (7/3) * shirts_profit

    # Calculate the profit from selling 3 pairs of sandals
    sandals_profit_total = (3/2) * sandals_profit

    # Calculate the total profit
    total_profit = shirts_profit_total + sandals_profit_total

    # return the result
    result = total_profit
    return result

print(solution())