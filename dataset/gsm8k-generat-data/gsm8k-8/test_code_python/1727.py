def solution():
    # Calculate the cost of all 9 pairs of socks
    total_cost = 9 * 2

    # Calculate the profit from the 4 pairs of socks with 25% profit
    profit_from_4_pairs = 4 * 0.25 * 2

    # Calculate the profit from the 5 pairs of socks with $0.2 profit each
    profit_from_5_pairs = 5 * 0.2

    # Calculate the total profit
    total_profit = profit_from_4_pairs + profit_from_5_pairs

    result = total_profit
    return result

print(solution())