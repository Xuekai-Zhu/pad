def solution():
    num_apples = 14
    num_oranges = 9
    num_blueberries = 6

    # Mary ate 1 of each fruit
    num_apples -= 1
    num_oranges -= 1
    num_blueberries -= 1

    # Calculate the total number of fruits left
    total_fruits_left = num_apples + num_oranges + num_blueberries
    result = total_fruits_left
    return result

print(solution())