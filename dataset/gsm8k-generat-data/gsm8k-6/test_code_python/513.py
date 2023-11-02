def solution():
    # Calculate the initial number of fruits
    pears = 10
    oranges = 20
    apples = 2 * pears
    total_fruits = pears + oranges + apples

    # Calculate the number of fruits after giving two of each to her sister
    pears -= 2
    oranges -= 2
    apples -= 2
    total_fruits_left = pears + oranges + apples

    result = total_fruits_left
    return result

print(solution())