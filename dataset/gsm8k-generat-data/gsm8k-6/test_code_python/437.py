def solution():
    # Calculate the total cost of chicken feed for selling all the chickens
    total_feed_cost = (2/20) * x * 2  # x is the number of chickens Lao sold
    # Calculate the total revenue from selling all the chickens
    total_revenue = 1.5 * x
    # Calculate the total profit
    total_profit = total_revenue - total_feed_cost
    # Solve for x using the profit equation
    x = (total_profit + (2/20) * x * 2) / 1.5
    result = round(x)
    return result

print(solution())