def solution():
     bars_bought = 5
     cost_per_bar = 5
     total_cost = bars_bought * cost_per_bar
     total_sales = 90
     packaging_cost = 2
     total_packaging_cost = packaging_cost * bars_bought
     profit = total_sales - (total_cost + total_packaging_cost)
     result = profit
     
     return result

print(solution())