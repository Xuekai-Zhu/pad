def solution():
    original_recipe_pasta = 2  # pounds
    original_recipe_servings = 7
    dale_family_size = 35

    # Calculate the ratio of pasta to servings in the original recipe
    pasta_to_servings_ratio = original_recipe_pasta / original_recipe_servings

    # Calculate how much pasta Dale needs for his family reunion
    dale_pasta = pasta_to_servings_ratio * dale_family_size

    result = dale_pasta
    return result

print(solution())