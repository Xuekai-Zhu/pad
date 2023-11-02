def solution():
    
    num_meals = 4
    meal_cost = 12
    num_apps = 2
    app_cost = 6
    tip_percent = 0.2
    rush_fee = 5
    
    subtotal = (num_meals * meal_cost) + (num_apps * app_cost)
    tip = subtotal * tip_percent
    total_cost = subtotal + tip + rush_fee
    
    result = total_cost
    return result

print(solution())