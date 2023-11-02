def solution():
    """A salesman bought a case of 48 backpacks for $576. He sold 17 of them for $18 at the swap meet, 10 were sold to a department store for $25 each. If the remainder were sold for $22 each. How much was the salesman's profit?"""
    # Define the original cost per backpack
    cost_per_backpack = 576 / 48

    # Calculate the revenue from selling 17 backpacks at $18 each
    revenue_swap_meet = 17 * 18

    # Calculate the revenue from selling 10 backpacks to the department store at $25 each
    revenue_department_store = 10 * 25

    # Calculate the cost of the backpacks sold to the department store
    cost_department_store = 10 * cost_per_backpack

    # Calculate the revenue from selling the remaining backpacks at $22 each
    revenue_remaining = (48 - 17 - 10) * 22

    # Calculate the cost of the remaining backpacks
    cost_remaining = (48 - 17 - 10) * cost_per_backpack

    # Calculate the total revenue and cost
    total_revenue = revenue_swap_meet + revenue_department_store + revenue_remaining
    total_cost = 576 + cost_remaining + cost_department_store

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())