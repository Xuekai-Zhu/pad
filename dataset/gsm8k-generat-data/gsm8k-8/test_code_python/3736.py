def solution():
    # Calculate the calories in the salad
    lettuce_calories = 50
    carrot_calories = 2 * lettuce_calories
    dressing_calories = 210
    total_salad_calories = lettuce_calories + carrot_calories + dressing_calories

    # Calculate the calories in the pizza
    crust_calories = 600
    pepperoni_calories = crust_calories / 3
    cheese_calories = 400
    total_pizza_calories = crust_calories + pepperoni_calories + cheese_calories

    # Calculate the calories Jackson eats
    jackson_salad_calories = 1/4 * total_salad_calories
    jackson_pizza_calories = 1/5 * total_pizza_calories

    total_calories = jackson_salad_calories + jackson_pizza_calories
    result = total_calories
    return result

print(solution())