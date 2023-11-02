def solution():
    # Calculate the calories in the salad
    lettuce_calories = 50
    carrot_calories = 2 * lettuce_calories
    dressing_calories = 210
    total_salad_calories = (lettuce_calories + carrot_calories + dressing_calories)
    quarter_salad_calories = total_salad_calories / 4

    # Calculate the calories in the pizza
    crust_calories = 600
    pepperoni_calories = crust_calories / 3
    cheese_calories = 400
    total_pizza_calories = (crust_calories + pepperoni_calories + cheese_calories)
    fifth_pizza_calories = total_pizza_calories / 5

    # Calculate the total calories Jackson will eat
    total_calories = quarter_salad_calories + fifth_pizza_calories
    result = total_calories
    return result

print(solution())