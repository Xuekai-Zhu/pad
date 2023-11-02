def solution():
    # Cost of 9 pairs of socks
    total_cost = 9 * 2

    # Profit from four pairs of socks with 25% markup
    markup_profit = 4 * 0.25 * 2

    # Profit from five pairs of socks with $0.2 profit each
    fixed_profit = 5 * 0.2

    # Total profit
    total_profit = markup_profit + fixed_profit

    # Final earnings
    earnings = total_cost + total_profit
    result = total_profit
    return result

print(solution())