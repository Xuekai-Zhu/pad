def solution():
    """Niko has bought 9 pairs of socks that cost $2 each and plans to resell them. He wants to gain 25% profit from four of the pairs of socks and $0.2 profit each for the other 5 pairs of socks. How much will his total profit be?"""
    # Define the cost of each pair of socks
    cost_per_pair = 2

    # Calculate the total cost of all 9 pairs of socks
    total_cost = cost_per_pair * 9

    # Calculate the profit from selling 4 pairs of socks with a 25% profit margin
    profit1 = 4 * (cost_per_pair * 1.25 - cost_per_pair)

    # Calculate the profit from selling 5 pairs of socks with a $0.2 profit
    profit2 = 5 * 0.2

    # Calculate the total profit
    total_profit = profit1 + profit2

    # return the result
    result = total_profit
    return result

print(solution())