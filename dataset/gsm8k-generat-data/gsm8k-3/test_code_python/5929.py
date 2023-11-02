def solution():
    """In a bowl of fruit, there are 2 bananas, twice as many apples, and some oranges. In total there are 12 fruits in the bowl. How many oranges are in the bowl?"""
    # Define the number of bananas and apples
    bananas = 2
    apples = 2 * bananas

    # Calculate the number of oranges
    oranges = 12 - bananas - apples

    # Display the number of oranges
    result = oranges
    return result

print(solution())