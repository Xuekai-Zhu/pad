def solution():
    
    total_fruit = 40
    apple_ratio = 3
    total_ratio = apple_ratio + 1
    orange_ratio = 1 / total_ratio
    total_oranges = total_fruit * orange_ratio
    result = total_oranges
    return result

print(solution())