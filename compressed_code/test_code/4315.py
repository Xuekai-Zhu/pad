def solution():
    
    blue_apples = 5
    yellow_apples = 2 * blue_apples
    total_apples = blue_apples + yellow_apples
    son_apples = total_apples / 5
    remaining_apples = total_apples - son_apples
    result = remaining_apples
    return result

print(solution())