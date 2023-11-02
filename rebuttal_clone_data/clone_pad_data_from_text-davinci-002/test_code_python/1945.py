def solution():
    max_weight = 20
    watermelon_weight = 1
    grapes_weight = 1
    oranges_weight = 1
    apple_weight = 1
    total_weight = watermelon_weight + grapes_weight + oranges_weight + apple_weight
    result = max_weight - total_weight
    return result

print(solution())