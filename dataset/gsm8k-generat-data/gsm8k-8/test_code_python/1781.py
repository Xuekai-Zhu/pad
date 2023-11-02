def solution():
    # Calculate the cost per backpack
    cost_per_backpack = 576 / 48

    # Calculate the revenue from selling 17 backpacks at $18 each
    revenue_swap_meet = 17 * 18

    # Calculate the revenue from selling 10 backpacks to department store at $25 each
    revenue_department_store = 10 * 25

    # Calculate the revenue from selling the remaining backpacks at $22 each
    remaining_backpacks = 48 - 17 - 10
    revenue_remaining = remaining_backpacks * 22

    # Calculate the total revenue and profit
    total_revenue = revenue_swap_meet + revenue_department_store + revenue_remaining
    total_cost = 576
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())