def solution():
    # Calculate the total number of planks John can make
    total_planks = 30 * 25

    # Calculate the number of tables John can make
    num_tables = total_planks // 15

    # Calculate the total revenue from selling the tables
    revenue = num_tables * 300

    # Calculate the total cost of labor
    labor_cost = 3000

    # Calculate the profit
    profit = revenue - labor_cost

    result = profit
    return result

print(solution())