def solution():
    # Calculate the total revenue from selling 17 backpacks at $18 each
    revenue_swap_meet = 17 * 18

    # Calculate the total revenue from selling 10 backpacks to the department store at $25 each
    revenue_department_store = 10 * 25

    # Calculate the total revenue from selling the remaining backpacks at $22 each
    remaining_backpacks = 48 - 17 - 10
    revenue_remaining_backpacks = remaining_backpacks * 22

    # Calculate the total cost of the backpacks
    cost_backpacks = 576

    # Calculate the total profit
    total_revenue = revenue_swap_meet + revenue_department_store + revenue_remaining_backpacks
    total_profit = total_revenue - cost_backpacks
    result = total_profit
    return result

print(solution())