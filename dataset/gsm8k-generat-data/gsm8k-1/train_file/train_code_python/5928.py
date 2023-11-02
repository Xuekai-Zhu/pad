def solution():
    """In a bowl of fruit, there are 2 bananas, twice as many apples, and some oranges. In total there are 12 fruits in the bowl. How many oranges are in the bowl?"""
    bananas = 2
    apples = bananas * 2
    total_fruits = 12
    oranges = total_fruits - bananas - apples
    result = oranges
    return result

print(solution())