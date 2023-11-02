def solution():
    oranges = 6
    apples = oranges - 2
    bananas = 3*apples
    peaches = bananas//2  # Use floor division to get an integer value

    total_fruit = oranges + apples + bananas + peaches
    result = total_fruit
    return result

print(solution())