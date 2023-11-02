def solution():
    # Define the cost and revenue per chicken
    cost_per_chicken = 2 + (2/20) * 1.5
    revenue_per_chicken = 1.5

    # Calculate the number of chickens sold
    profit = 65
    num_chickens_sold = int(profit / (revenue_per_chicken - cost_per_chicken))

    result = num_chickens_sold
    return result

print(solution())