def solution():
    
    total_apples = 30
    small_apples = total_apples / 6
    unripe_apples = total_apples / 3
    perfect_apples = total_apples - small_apples - unripe_apples
    result = perfect_apples
    return result

print(solution())