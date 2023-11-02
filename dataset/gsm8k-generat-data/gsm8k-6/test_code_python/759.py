def solution():
    # Calculate the cost of flour and salt
    cost_flour = (500 / 50) * 20  # 500 pounds of flour and 50-pound bags of flour cost $20
    cost_salt = 10 * 0.2  # 10 pounds of salt and salt costs $.2 a pound

    # Calculate the total cost
    total_cost = cost_flour + cost_salt + 1000  # add the cost of flour, salt and promotion

    # Calculate the total revenue
    total_revenue = 500 * 20  # 500 tickets sold for $20 each

    # Calculate the profit
    profit = total_revenue - total_cost

    result = profit
    return result

print(solution())