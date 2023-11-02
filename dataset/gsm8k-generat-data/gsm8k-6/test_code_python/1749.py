def solution():
    # Calculate the total number of planks John can make
    total_planks = 30 * 25

    # Calculate the number of tables John can make
    num_tables = total_planks // 15

    # Calculate the total revenue from selling the tables
    total_revenue = num_tables * 300

    # Calculate the total cost of labor
    total_labor_cost = 3000

    # Calculate the profit
    profit = total_revenue - total_labor_cost

    result = profit
    return result

print(solution())