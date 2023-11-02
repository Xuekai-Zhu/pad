def solution():
    lettuce_calories = 50
    carrot_calories = 2 * lettuce_calories
    dressing_calories = 210
    total_salad_calories = lettuce_calories + (3 * carrot_calories) + dressing_calories
    pizza_crust_calories = 600
    pepperoni_calories = pizza_crust_calories / 3
    cheese_calories = 400
    total_pizza_calories = pizza_crust_calories + pepperoni_calories + cheese_calories
    salad_portion = total_salad_calories / 4
    pizza_portion = total_pizza_calories / 5
    total_calories = salad_portion + pizza_portion
    result = total_calories
    return result

print(solution())