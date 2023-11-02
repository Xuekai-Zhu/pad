def solution():
    """In a bowl of fruit, there are 2 bananas, twice as many apples, and some oranges.
    In total there are 12 fruits in the bowl. How many oranges are in the bowl?"""
    # Define the number of bananas
    bananas = 2

    # Calculate the number of apples
    apples = 2 * bananas

    # Calculate the number of oranges
    oranges = 12 - bananas - apples

    # Return the result
    result = oranges
    return result

print(solution())