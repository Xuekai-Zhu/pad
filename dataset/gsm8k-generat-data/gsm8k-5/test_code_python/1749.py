def solution():
    trees_chopped = 30  # John chops down 30 trees
    planks_per_tree = 25  # John can make 25 planks from each tree
    planks_per_table = 15  # It takes 15 planks to make a table
    table_price = 300  # John sells each table for $300
    labor_cost = 3000  # John paid $3000 for all the labor

    # Calculate the total number of planks John can make from the trees
    total_planks = trees_chopped * planks_per_tree

    # Calculate the total number of tables John can make from the planks
    total_tables = total_planks // planks_per_table

    # Calculate the total revenue John earns from selling the tables
    total_revenue = total_tables * table_price

    # Calculate John's profit after deducting the labor cost
    profit = total_revenue - labor_cost
    result = profit
    return result

print(solution())