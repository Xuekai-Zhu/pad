def solution():
     initial_cost = 3
     eggs_per_snake = 2
     average_sale_price = 250
     rare_sale_price = average_sale_price * 4
     total_eggs = initial_cost * eggs_per_snake
     total_revenue = (total_eggs - 1) * average_sale_price + rare_sale_price
     result = total_revenue
     return result

print(solution())