def solution():
    apples_1 = 200
    apples_2 = apples_1 - (apples_1 * 20 / 100)
    apples_3 = apples_2 * 2
    total_apples = apples_1 + apples_2 + apples_3
    result = total_apples
    return result

print(solution())