def solution():
    # Calculate the total calories in the salad
    lettuce_calories = 50
    carrots_calories = 2 * lettuce_calories
    dressing_calories = 210
    total_salad_calories = lettuce_calories + carrots_calories + dressing_calories

    # Calculate the total calories in the pizza
    crust_calories = 600
    pepperoni_calories = crust_calories / 3
    cheese_calories = 400
    total_pizza_calories = crust_calories + pepperoni_calories + cheese_calories

    # Calculate the calories Jackson eats
    calories_from_salad = total_salad_calories / 4
    calories_from_pizza = total_pizza_calories / 5
    total_calories_eaten = calories_from_salad + calories_from_pizza

    result = total_calories_eaten
    return result

print(solution())