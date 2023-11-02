def solution():
    
    total_trees = 30
    planks_per_tree = 25
    total_planks = total_trees * planks_per_tree
    planks_per_table = 15
    tables = total_planks // planks_per_table
    table_price = 300
    total_table_price = tables * table_price
    labor_cost = 3000
    profit = total_table_price - labor_cost
    result = profit
    return result

print(solution())