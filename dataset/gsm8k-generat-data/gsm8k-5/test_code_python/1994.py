def solution():
    oranges = 40
    apples = 70

    # Calculate the number of oranges and apples sold
    oranges_sold = oranges / 4
    apples_sold = apples / 2

    # Calculate the remaining number of oranges and apples
    remaining_oranges = oranges - oranges_sold
    remaining_apples = apples - apples_sold

    # Calculate the total number of fruits left
    total_fruits = remaining_oranges + remaining_apples
    result = total_fruits
    return result

print(solution())