def solution():
    num_woodburning = 20
    price_per_woodburning = 15
    wood_cost = 100

    # Calculate the total revenue from selling all woodburning
    total_revenue = num_woodburning * price_per_woodburning

    # Calculate the total profit from selling all woodburning
    total_profit = total_revenue - wood_cost

    result = total_profit
    return result

print(solution())