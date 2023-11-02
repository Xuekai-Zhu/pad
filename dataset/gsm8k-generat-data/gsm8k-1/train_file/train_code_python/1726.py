def solution():
    """Niko has bought 9 pairs of socks that cost $2 each and plans to resell them. He wants to gain 25% profit from four of the pairs of socks and $0.2 profit each for the other 5 pairs of socks. How much will his total profit be?"""
    num_pairs = 9
    pair_cost = 2
    four_pairs_profit = 0.25 * pair_cost * 4
    five_pairs_profit = 0.2 * 5

    total_profit = four_pairs_profit + five_pairs_profit
    result = total_profit
    
    return result

print(solution())