def solution():
     total_cupcakes_sold = 50
     total_cookies_sold = 40
     total_sales = (total_cupcakes_sold * 2) + (total_cookies_sold * 0.5)
     total_cost_of_basketballs = 40 * 2
     total_cost_of_energy_drinks = total_sales - total_cost_of_basketballs
     cost_of_one_energy_drink = total_cost_of_energy_drinks / 20
     result = cost_of_one_energy_drink
 
     return result

print(solution())