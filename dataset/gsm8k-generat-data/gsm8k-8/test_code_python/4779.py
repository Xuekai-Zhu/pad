def solution():
    # Calculate profit from selling 3 shirts
    shirt_profit = 21 / 3

    # Calculate profit from selling 2 pairs of sandals
    sandal_profit = 4 * shirt_profit

    # Calculate total profit from selling 7 shirts and 3 pairs of sandals
    total_profit = 7 * shirt_profit + 3 * sandal_profit
    result = total_profit
    return result

print(solution())