def solution():
    # Define the costs and revenue for each item
    doll_cost = 3 * 5
    clock_cost = 2 * 15
    glass_cost = 5 * 4
    total_cost = doll_cost + clock_cost + glass_cost
    revenue = total_cost + 40

    # Calculate the profit
    profit = revenue - total_cost
    result = profit
    return result

print(solution())