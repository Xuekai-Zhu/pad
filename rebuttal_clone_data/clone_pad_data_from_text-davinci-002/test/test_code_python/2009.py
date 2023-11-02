def solution():
     machine_parts_cost = 3600
     machine_patent_cost = 4500
     machine_sale_price = 180
     total_cost = machine_parts_cost + machine_patent_cost
     number_of_sales = total_cost / machine_sale_price
     result = number_of_sales
     return result

print(solution())