def solution():
    # Louis has 5 oranges and 3 apples
    louis_oranges = 5
    louis_apples = 3

    # Samantha has 8 oranges and 7 apples
    samantha_oranges = 8
    samantha_apples = 7

    # Marley has twice as many oranges as Louis
    marley_oranges = 2 * louis_oranges

    # Marley has three times as many apples as Samantha
    marley_apples = 3 * samantha_apples

    # Calculate the total number of fruits that Marley has
    total_fruits = marley_oranges + marley_apples
    result = total_fruits
    return result

print(solution())