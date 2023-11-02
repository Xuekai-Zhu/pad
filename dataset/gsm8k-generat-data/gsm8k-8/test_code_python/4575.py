def solution():
    # Calculate the profit from the large posters
    large_profit = 2 * (10 - 5)

    # Calculate the profit from the small posters
    small_profit = (5-2) * (6 - 3)

    # Calculate the total profit for 5 days
    total_profit = 5 * (large_profit + small_profit)

    result = total_profit
    return result

print(solution())