def solution():
    
    lettuce_calories = 50
    carrot_calories = lettuce_calories * 2
    dressing_calories = 210
    salad_total_calories = lettuce_calories + carrot_calories + dressing_calories
    pizza_crust_calories = 600
    pepperoni_calories = pizza_crust_calories / 3
    cheese_calories = 400
    pizza_total_calories = pizza_crust_calories + pepperoni_calories + cheese_calories
    
    
    eaten_salad_calories = salad_total_calories / 4
    eaten_pizza_calories = pizza_total_calories / 5
    
    total_calories = eaten_salad_calories + eaten_pizza_calories
    result = total_calories
    return result

print(solution())