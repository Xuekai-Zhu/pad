def solution():
    burritos_cost = 6
    burritos_calories = 120
    burgers_cost = 8
    burgers_calories = 400
    
    calories_per_dollar_burritos = burritos_calories / burritos_cost
    calories_per_dollar_burgers = burgers_calories / burgers_cost
    
    result = calories_per_dollar_burgers - calories_per_dollar_burritos
    
    return result

print(solution())