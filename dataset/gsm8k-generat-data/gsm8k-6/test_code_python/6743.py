def solution():
    # Calculate the total cost of feeding the cattle
    feeding_cost = 40000 * 1.2 - 40000  # 20% more than the cost of buying them

    # Calculate the total weight of the cattle
    total_weight = 100 * 1000

    # Calculate the total revenue from selling the cattle
    total_revenue = total_weight * 2

    # Calculate the profit made
    profit = total_revenue - (40000 + feeding_cost)
    result = profit
    return result

print(solution())