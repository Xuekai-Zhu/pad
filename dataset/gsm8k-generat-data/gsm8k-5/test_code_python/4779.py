def solution():
    # Profit from selling 3 shirts
    profit_shirts = 21

    # Profit from selling 2 pairs of sandals
    profit_sandals = 4 * profit_shirts

    # Calculate the total profit from selling 7 shirts
    profit_shirts_total = (7 // 3) * profit_shirts

    # Calculate the total profit from selling 3 pairs of sandals
    profit_sandals_total = (3 // 2) * profit_sandals

    # Calculate the total profit
    total_profit = profit_shirts_total + profit_sandals_total
    result = total_profit
    return result

print(solution())