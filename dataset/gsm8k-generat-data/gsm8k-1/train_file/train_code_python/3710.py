def solution():
    """If Katherine has 4 apples and 3 times as many pears in her fridge, how many bananas does she have if she has a total of 21 pieces of fruit?"""
    apples = 4
    pears = 3 * apples
    total_fruit = 21
    bananas = total_fruit - (apples + pears)
    result = bananas
    return result

print(solution())