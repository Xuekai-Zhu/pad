def solution():
    
    total_apples = 85
    wormy_apples = total_apples / 5
    bruised_apples = (1/5 * total_apples) + 9
    raw_apples = total_apples - wormy_apples - bruised_apples
    result = raw_apples
    return result

print(solution())