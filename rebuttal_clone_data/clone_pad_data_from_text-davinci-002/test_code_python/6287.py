def solution():
     daily_production = 1000
     production_cost = 250
     tire_sale_price = production_cost * 1.5
     potential_sales = 1200
     total_loss = potential_sales - daily_production
     weekly_loss = total_loss * 7
     result = weekly_loss
     return result

print(solution())