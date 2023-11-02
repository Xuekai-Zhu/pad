def solution():
    
    lettuce_calories = 50
    carrots_calories = 2 * lettuce_calories
    dressing_calories = 210
    salad_calories = lettuce_calories + carrots_calories + dressing_calories
    pizza_crust_calories = 600
    pepperoni_calories = pizza_crust_calories / 3
    cheese_calories = 400
    pizza_calories = pizza_crust_calories + pepperoni_calories + cheese_calories
    jackson_salad_calories = 1/4 * salad_calories
    jackson_pizza_calories = 1/5 * pizza_calories
    total_calories = jackson_salad_calories + jackson_pizza_calories
    result = total_calories
    return result

print(solution())