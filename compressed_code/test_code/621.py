def solution():
    
    starting_apples = 74
    ricki_removes = 14
    samson_removes = 2 * ricki_removes
    remaining_apples = starting_apples - ricki_removes - samson_removes
    result = remaining_apples
    return result

print(solution())