def solution():
    """Louis has 5 oranges and 3 apples. Samantha has 8 oranges and 7 apples. If Marley has twice as many oranges as Louis and three times as many apples as Samantha, how many fruits in total does Marley have?"""
    louis_oranges = 5
    louis_apples = 3
    samantha_oranges = 8
    samantha_apples = 7
    marley_oranges = 2 * louis_oranges
    marley_apples = 3 * samantha_apples
    total_fruits = louis_oranges + louis_apples + samantha_oranges + samantha_apples + marley_oranges + marley_apples
    result = total_fruits
    return result

print(solution())