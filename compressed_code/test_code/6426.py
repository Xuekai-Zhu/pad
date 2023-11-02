def solution():
    
    initial_apples = 74
    ricki_removed = 14
    samson_removed = ricki_removed * 2
    apples_left = initial_apples - ricki_removed - samson_removed
    result = apples_left
    return result

print(solution())