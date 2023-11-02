def solution():
    # Calculate the cost of feeding the cattle
    feed_cost = 40000 * 1.2

    # Calculate the total cost of the cattle
    total_cost = 40000 + feed_cost

    # Calculate the total weight of the cattle
    total_weight = 100 * 1000

    # Calculate the revenue from selling the cattle
    revenue = total_weight * 2

    # Calculate the profit
    profit = revenue - total_cost
    result = profit
    return result

print(solution())