def solution():
    # Calculate the total number of fruit in the basket
    oranges = 6
    apples = oranges - 2
    bananas = 3 * apples
    peaches = int(bananas / 2)  # use integer division since we cannot have half a fruit
    total_fruit = oranges + apples + bananas + peaches
    result = total_fruit
    return result

print(solution())