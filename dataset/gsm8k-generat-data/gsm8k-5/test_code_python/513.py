def solution():
    pears = 10
    oranges = 20
    apples = 2 * pears

    # Calculate the total number of fruits Jennifer has
    total_fruits = pears + oranges + apples

    # Calculate the number of fruits Jennifer gives to her sister
    fruits_given = 2 * (pears + oranges + apples)

    # Calculate the number of fruits Jennifer has left
    fruits_left = total_fruits - fruits_given
    result = fruits_left
    return result

print(solution())