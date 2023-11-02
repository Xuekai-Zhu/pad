def solution():
    # Define the number of oranges and apples Tom started with
    oranges = 40
    apples = 70

    # Calculate how many oranges and apples Tom sold
    oranges_sold = oranges / 4
    apples_sold = apples / 2

    # Calculate how many oranges and apples Tom has left
    oranges_left = oranges - oranges_sold
    apples_left = apples - apples_sold

    # Calculate the total number of fruits Tom has left
    fruits_left = oranges_left + apples_left
    result = fruits_left
    return result

print(solution())