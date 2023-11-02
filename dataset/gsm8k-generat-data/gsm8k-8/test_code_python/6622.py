def solution():
    # Calculate the number of oranges and apples Louis has
    louis_oranges = 5
    louis_apples = 3

    # Calculate the number of oranges and apples Samantha has
    samantha_oranges = 8
    samantha_apples = 7

    # Calculate the number of oranges and apples Marley has
    marley_oranges = 2 * louis_oranges
    marley_apples = 3 * samantha_apples

    # Calculate the total number of fruits Marley has
    total_fruits = marley_oranges + marley_apples
    result = total_fruits
    return result

print(solution())