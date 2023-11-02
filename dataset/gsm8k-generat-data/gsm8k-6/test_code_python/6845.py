def solution():
    # Calculate the cost of the apples and oranges
    cost_of_apples = (3/2) * 5  # the vendor bought apples at 2 for $3, so 5 apples cost $7.50
    cost_of_oranges = 2.7  # the vendor bought 3 oranges for $2.70, so each orange cost $0.90
    total_cost = cost_of_apples + cost_of_oranges  # the total cost of the fruits

    # Calculate the revenue from selling 5 apples and 5 oranges
    revenue_from_apples = (10/5) * 5  # the vendor plans to sell 5 apples for $10, so the revenue is $10
    revenue_from_oranges = 5  # the vendor plans to sell 5 oranges for $1 each, so the revenue is $5
    total_revenue = revenue_from_apples + revenue_from_oranges  # the total revenue from selling the fruits

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())