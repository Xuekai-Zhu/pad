def solution():
    # Calculate the profit from selling 3 shirts
    profit_shirts = 21  # Melony makes $21 of profit every time she sells 3 shirts

    # Calculate the profit from selling 2 pairs of sandals
    profit_sandals = 4 * profit_shirts  # four times as much profit as selling 3 shirts

    # Calculate the total profit from selling 7 shirts and 3 pairs of sandals
    total_profit = (7 // 3) * profit_shirts + (3 // 2) * profit_sandals

    result = total_profit
    return result

print(solution())