def solution():
    num_servings = 8
    vegetables_per_serving = 1 # in cups
    broth_per_serving = 2.5 # in cups
    cups_per_pint = 2 # there are 2 cups in 1 pint

    # Calculate the total cups of vegetables needed for 8 servings
    total_veggies = num_servings * vegetables_per_serving

    # Calculate the total cups of broth needed for 8 servings
    total_broth = num_servings * broth_per_serving

    # Calculate the total cups of vegetables and broth combined
    total_combined = total_veggies + total_broth

    # Convert total combined cups to pints
    total_pints = total_combined / cups_per_pint

    result = total_pints
    return result

print(solution())