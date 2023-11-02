def solution():
    """John chops down 30 trees.  From each tree, he can make 25 planks.  A table takes 15 planks to make and sells for $300.  He paid $3000 for all the labor.  How much profit did he make?"""
    # Define the number of trees John chops down
    num_trees = 30

    # Define the number of planks John can make from each tree
    planks_per_tree = 25

    # Calculate the total number of planks John can make
    total_planks = num_trees * planks_per_tree

    # Calculate the number of tables John can make
    num_tables = total_planks // 15

    # Calculate the total revenue from selling the tables
    revenue = num_tables * 300

    # Calculate the total cost of labor
    labor_cost = 3000

    # Calculate the profit
    profit = revenue - labor_cost

    # Display the profit
    result = profit
    return result

print(solution())