def solution():
    # Define the initial quantities of fruit
    apples = 14
    oranges = 9
    blueberries = 6

    # Subtract one from each fruit
    apples -= 1
    oranges -= 1
    blueberries -= 1

    # Calculate the total number of fruit left
    total_fruit = apples + oranges + blueberries
    result = total_fruit
    return result

print(solution())