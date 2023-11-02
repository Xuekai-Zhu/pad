def solution():
     small_pizza_price = 2
     large_pizza_price = 8
     total_sales = 40
     total_small_pizzas_sold = 8
     total_large_pizzas_sold = (total_sales - (total_small_pizzas_sold * small_pizza_price)) / large_pizza_price
     result = total_large_pizzas_sold
     return result

print(solution())