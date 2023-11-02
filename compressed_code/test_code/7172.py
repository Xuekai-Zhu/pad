def solution():
    
    trees_chopped = 30
    planks_per_tree = 25
    planks_per_table = 15
    tables_per_tree = planks_per_tree / planks_per_table
    total_tables = trees_chopped * tables_per_tree
    table_price = 300
    labor_cost = 3000
    revenue = total_tables * table_price
    profit = revenue - labor_cost
    result = profit
    return result

print(solution())