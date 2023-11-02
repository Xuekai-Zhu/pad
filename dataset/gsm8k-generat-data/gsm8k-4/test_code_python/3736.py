def solution():
    """Jackson is making dinner. He makes a salad out of lettuce (50 calories), carrots (twice the calories of the lettuce) and dressing (210 calories). He also makes a pizza with 600 calories for the crust, 1/3 the crust's calories for the pepperoni, and 400 calories for the cheese. If Jackson eats 1/4 of the salad and 1/5 of the pizza, how many calories does he eat?"""
    # Calculate the total number of calories in the salad
    lettuce_calories = 50
    carrots_calories = 2 * lettuce_calories
    dressing_calories = 210
    total_salad_calories = lettuce_calories + carrots_calories + dressing_calories

    # Calculate the number of calories in the portion of salad that Jackson eats
    salad_portion = 1/4
    jackson_salad_calories = total_salad_calories * salad_portion

    # Calculate the total number of calories in the pizza
    crust_calories = 600
    pepperoni_calories = 1/3 * crust_calories
    cheese_calories = 400
    total_pizza_calories = crust_calories + pepperoni_calories + cheese_calories

    # Calculate the number of calories in the portion of pizza that Jackson eats
    pizza_portion = 1/5
    jackson_pizza_calories = total_pizza_calories * pizza_portion

    # Calculate the total number of calories that Jackson eats
    total_calories = jackson_salad_calories + jackson_pizza_calories

    # return the result
    result = total_calories
    return result

print(solution())