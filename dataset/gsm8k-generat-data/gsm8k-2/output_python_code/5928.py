def solution():
    """In a bowl of fruit, there are 2 bananas, twice as many apples, and some oranges. In total there are 12 fruits in the bowl. How many oranges are in the bowl?"""
    total_fruits = 12
    bananas = 2
    apples = 2 * bananas
    oranges = total_fruits - bananas - apples
    result = oranges
    return result

print(solution())