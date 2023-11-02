def solution():
    num_pears = 10
    num_oranges = 20
    num_apples = num_pears * 2

    # Subtract two of each fruit given to the sister
    num_pears -= 2
    num_oranges -= 2
    num_apples -= 2

    # Calculate the total number of fruits left
    num_fruits_left = num_pears + num_oranges + num_apples
    result = num_fruits_left
    return result

print(solution())