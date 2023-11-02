def solution():
    """One serving of soup has 1 cup of vegetables and 2.5 cups of broth. How many pints of vegetables and broth combined would be needed for 8 servings?"""
    cups_per_serving = 3.5
    servings = 8
    cups_needed = cups_per_serving * servings
    pints_needed = cups_needed / 2
    result = pints_needed
    return result

print(solution())