def solution():
    bella_apples_per_day = 6
    weeks = 6
    grace_apples = 0

    for i in range(weeks):
        grace_apples += (bella_apples_per_day * 7) / 3

    result = grace_apples
    return result

print(solution())