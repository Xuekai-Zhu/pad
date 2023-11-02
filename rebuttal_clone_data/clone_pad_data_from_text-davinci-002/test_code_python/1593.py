def solution():
    yun_initial = 20
    yun_lost = 12
    yun_current = yun_initial - yun_lost
    marion_increase = yun_current * (1/4)
    marion_total = yun_current + marion_increase + 7
    result = marion_total
    return result

print(solution())