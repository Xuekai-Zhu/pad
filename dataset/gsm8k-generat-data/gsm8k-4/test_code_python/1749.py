def solution():
    """John chops down 30 trees. From each tree, he can make 25 planks. A table takes 15 planks to make and sells for $300. He paid $3000 for all the labor. How much profit did he make?"""
    # Define the number of trees and planks
    NUM_TREES = 30
    PLANKS_PER_TREE = 25

    # Calculate the total number of planks
    total_planks = NUM_TREES * PLANKS_PER_TREE

    # Calculate the number of tables that can be made
    num_tables = total_planks // 15

    # Calculate the total revenue from selling tables
    total_revenue = num_tables * 300

    # Calculate the total cost of labor
    total_labor_cost = 3000

    # Calculate the profit
    profit = total_revenue - total_labor_cost

    # return the result
    result = profit
    return result

print(solution())