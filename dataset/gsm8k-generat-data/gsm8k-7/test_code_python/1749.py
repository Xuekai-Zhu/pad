def solution():
    num_trees = 30
    planks_per_tree = 25
    planks_per_table = 15
    table_price = 300
    labor_cost = 3000

    # Calculate the total number of planks John can make
    total_planks = num_trees * planks_per_tree

    # Calculate the total number of tables John can make
    total_tables = total_planks // planks_per_table

    # Calculate the total revenue from selling all the tables
    total_revenue = total_tables * table_price

    # Calculate the total profit
    total_profit = total_revenue - labor_cost
    result = total_profit
    return result

print(solution())