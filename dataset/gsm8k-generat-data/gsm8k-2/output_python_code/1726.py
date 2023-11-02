def solution():
    """Niko has bought 9 pairs of socks that cost $2 each and plans to resell them. He wants to gain 25% profit from four of the pairs of socks and $0.2 profit each for the other 5 pairs of socks. How much will his total profit be?"""
    sock_cost = 2
    total_cost = sock_cost * 9
    profit_four = 0.25 * sock_cost * 4
    profit_five = 0.2 * 5
    total_profit = profit_four + profit_five
    result = total_profit
    return result

print(solution())