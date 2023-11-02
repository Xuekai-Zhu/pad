def solution():
    """Louis has 5 oranges and 3 apples. Samantha has 8 oranges and 7 apples. If Marley has twice as many oranges as Louis and three times as many apples as Samantha, how many fruits in total does Marley have?"""
    louis_oranges = 5
    louis_apples = 3
    samantha_oranges = 8
    samantha_apples = 7
    marley_oranges = louis_oranges * 2
    marley_apples = samantha_apples * 3
    total_fruits = marley_oranges + marley_apples
    result = total_fruits
    
    return result

print(solution())