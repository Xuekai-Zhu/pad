def solution():
    num_dozens = 5
    cost_per_dozen = 2.40
    selling_price_per_egg = 1
    num_eggs_per_dozen = 3

    # Calculate the total cost of all dozens of eggs
    total_cost = num_dozens * cost_per_dozen

    # Calculate the total revenue from selling all eggs
    total_revenue = num_eggs_per_dozen * selling_price_per_egg

    # Calculate the total cost of all eggs
    total_cost = total_cost + total_revenue

    # Calculate Rose's profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())