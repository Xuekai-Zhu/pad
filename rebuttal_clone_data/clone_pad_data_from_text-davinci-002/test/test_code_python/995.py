def solution():
     trees_chopped = 30
     planks_per_tree = 25
     planks_needed_per_table = 15
     table_sale_price = 300
     initial_labor_cost= 3000
     total_planks = trees_chopped * planks_per_tree
     total_tables_made = total_planks / planks_needed_per_table
     total_sales = total_tables_made * table_sale_price
     profit = total_sales - initial_labor_cost
     result = profit
     return result

print(solution())