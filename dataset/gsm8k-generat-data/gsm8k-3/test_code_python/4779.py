def solution():
    """Melony makes $21 of profit every time she sells 3 shirts and four times as much profit when she sells two pairs of sandals. How much profit will she make if she sells 7 shirts and 3 pairs of sandals?"""
    # Calculate the profit from selling shirts
    shirts_profit = 7 // 3 * 21

    # Calculate the profit from selling sandals
    sandals_profit = 3 * 4 * 21

    # Calculate the total profit
    total_profit = shirts_profit + sandals_profit

    # Display the total profit
    result = total_profit
    return result

print(solution())