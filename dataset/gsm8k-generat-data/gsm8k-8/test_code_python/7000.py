def solution():
    # Define the cost and selling prices for each candy bar
    cost_per_bar = 80
    selling_price_per_bar = 100

    # Calculate the total cost and revenue
    total_cost = 50 * cost_per_bar
    total_revenue = 48 * selling_price_per_bar

    # Calculate the profit in cents
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())