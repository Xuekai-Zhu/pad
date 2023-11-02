def solution():
    num_oranges = 6
    num_apples = num_oranges - 2
    num_bananas = 3 * num_apples
    num_peaches = num_bananas / 2

    # Calculate the total number of pieces of fruit in the basket
    total_fruit = num_oranges + num_apples + num_bananas + num_peaches
    result = total_fruit
    return result

print(solution())