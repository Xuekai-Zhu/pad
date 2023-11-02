def solution():
    """One serving of soup has 1 cup of vegetables and 2.5 cups of broth. How many pints of vegetables and broth combined would be needed for 8 servings?"""
    cups_veggies_per_serving = 1
    cups_broth_per_serving = 2.5
    total_cups_veggies = cups_veggies_per_serving * 8
    total_cups_broth = cups_broth_per_serving * 8
    total_pints = (total_cups_veggies + total_cups_broth) / 2
    result = total_pints
    return result

print(solution())