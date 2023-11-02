def solution():
    yun_initial = 20
    yun_lost = 12
    yun_current = yun_initial - yun_lost

    marion_current = yun_current * 1.25 + 7
    result = marion_current
    return result

print(solution())