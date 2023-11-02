def solution():
    louis_oranges = 5
    louis_apples = 3
    samantha_oranges = 8
    samantha_apples = 7
    marley_oranges = 2 * louis_oranges  # Marley has twice as many oranges as Louis
    marley_apples = 3 * samantha_apples  # Marley has three times as many apples as Samantha

    # Calculate the total number of fruits Marley has
    total_fruits = marley_oranges + marley_apples
    result = total_fruits
    return result

print(solution())