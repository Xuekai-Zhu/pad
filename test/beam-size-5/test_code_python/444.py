def solution():
    # Calculate the total revenue from selling 17 sneakers on Monday
    revenue_monday = 17 * 20

    # Calculate the total revenue from selling 17 sneakers to the department store
    revenue_department_store = 25 * (48 - 17)

    # Calculate the total cost of the sneakers
    total_cost = 576

    # Calculate the total revenue from selling 17 sneakers to the department store
    revenue_department_store = revenue_department_store * (48 - 17)

    # Calculate the total profit
    total_profit = revenue_monday + revenue_department_store
    result = total_profit
    return result

print(solution())