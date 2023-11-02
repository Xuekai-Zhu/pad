def solution():
    """Jackson is making dinner. He makes a salad out of lettuce (50 calories), carrots (twice the calories of the lettuce) and dressing (210 calories). He also makes a pizza with 600 calories for the crust, 1/3 the crust's calories for the pepperoni, and 400 calories for the cheese. If Jackson eats 1/4 of the salad and 1/5 of the pizza, how many calories does he eat?"""
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