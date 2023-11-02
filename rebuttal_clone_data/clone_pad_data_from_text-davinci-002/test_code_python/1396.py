def solution():
    morning_milk = 68
    evening_milk = 82
    today_morning_milk = morning_milk - 18
    sold_milk = morning_milk + evening_milk - today_morning_milk - 24
    price_per_gallon = 3.50
    total_revenue = sold_milk * price_per_gallon
    result = total_revenue
    
    return result

print(solution())