def solution():
     cost_per_acre = 70
     acres_bought = 200
     development_cost = cost_per_acre * acres_bought
     acres_sold = acres_bought / 2
     sale_price_per_acre = 200
     sale_price = acres_sold * sale_price_per_acre
     profit = sale_price - development_cost
     result = profit
 
     return result

print(solution())