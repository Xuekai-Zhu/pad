def solution():
    tuesday_apples = 4
    wednesday_apples = 2 * tuesday_apples
    thursday_apples = 0.5 * tuesday_apples

    total_apples = tuesday_apples + wednesday_apples + thursday_apples
    result = total_apples
    return result

print(solution())