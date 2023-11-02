def solution():
    # Calculate Niko's total cost for buying the socks
    total_cost = 9 * 2  # each pair of socks costs $2

    # Calculate Niko's profit for the four pairs of socks with 25% markup
    profit_markup = 4 * ((25/100) * 2)  # 25% profit for each pair of socks with a $2 cost

    # Calculate Niko's profit for the five pairs of socks with $0.2 profit each
    profit_fixed = 5 * 0.2  # $0.2 profit for each pair of socks

    # Calculate Niko's total profit
    total_profit = profit_markup + profit_fixed

    result = total_profit
    return result

print(solution())