def solution():
    """One serving of soup has 1 cup of vegetables and 2.5 cups of broth. How many pints of vegetables and broth combined would be needed for 8 servings?"""
    # Define the amounts per serving in cups
    VEGETABLES_PER_SERVING = 1
    BROTH_PER_SERVING = 2.5

    # Calculate the total amounts needed for 8 servings in cups
    total_vegetables = VEGETABLES_PER_SERVING * 8
    total_broth = BROTH_PER_SERVING * 8

    # Convert the amounts to pints
    total_vegetables_pints = total_vegetables / 2
    total_broth_pints = total_broth / 2

    # Calculate the total combined amount in pints
    total_pints = total_vegetables_pints + total_broth_pints

    # Display the total combined amount in pints
    result = total_pints
    return result

print(solution())