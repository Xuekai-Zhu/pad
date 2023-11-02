def solution():
    # Calculate the number of apples
    oranges = 6
    apples = oranges - 2

    # Calculate the number of bananas
    bananas = 3 * apples

    # Calculate the number of peaches
    peaches = bananas / 2

    # Calculate the total number of pieces of fruit
    total_fruit = oranges + apples + bananas + peaches
    result = total_fruit
    return result

print(solution())