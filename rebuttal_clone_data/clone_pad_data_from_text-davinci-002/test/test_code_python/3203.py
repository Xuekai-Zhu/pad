def solution():
     purchase_price = 600
     daily_food_cost = 20
     vaccination_and_deworming_cost = 500
     total_cost = purchase_price + (daily_food_cost * 40) + vaccination_and_deworming_cost
     sale_price = 2500
     profit = sale_price - total_cost
     result = profit
     return result

print(solution())