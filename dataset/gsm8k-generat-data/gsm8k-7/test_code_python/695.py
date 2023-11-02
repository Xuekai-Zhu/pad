def solution():
    watermelon_puree = 500  # in ml
    cream = 100  # in ml
    serving_size = 150  # in ml

    # Determine the total amount of liquid for each serving
    total_liquid_per_serving = watermelon_puree + cream

    # Determine the number of servings that can be made
    num_servings = total_liquid_per_serving // serving_size

    result = num_servings
    return result

print(solution())