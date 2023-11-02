def solution():
     milk_produced = 200
     days_in_month = 30
     total_milk = milk_produced * days_in_month
     price_per_gallon = 3.55
     total_income = total_milk * price_per_gallon
     result = total_income - 3000
     return result

print(solution())