def solution():
    # Calculate profit from selling 3 shirts
    profit_3_shirts = 21

    # Calculate profit from selling 2 pairs of sandals
    profit_2_sandals = 4 * profit_3_shirts

    # Calculate profit from selling 7 shirts and 3 pairs of sandals
    total_profit = (7/3) * profit_3_shirts + (3/2) * profit_2_sandals
    result = total_profit
    return result

print(solution())