def solution():
     seed_cost = 2
     soil_cost = 8
     number_of_plants = 20
     sale_price = 5
     total_revenue = number_of_plants * sale_price
     total_cost = seed_cost + soil_cost
     net_profit = total_revenue - total_cost
     result = net_profit
     return result

print(solution())