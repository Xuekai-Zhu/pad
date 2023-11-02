def solution():
    """One serving of soup has 1 cup of vegetables and 2.5 cups of broth. How many pints of vegetables and broth combined would be needed for 8 servings?"""
    # Define the measurements in cups per serving
    vegetables_per_serving = 1
    broth_per_serving = 2.5

    # Calculate the total measurements needed for 8 servings
    vegetables_total = vegetables_per_serving * 8
    broth_total = broth_per_serving * 8

    # Convert the measurements to pints
    vegetables_pints = vegetables_total / 2
    broth_pints = broth_total / 2

    # Calculate the combined pints needed
    pints_combined = vegetables_pints + broth_pints

    result = pints_combined
    return result

print(solution())