def solution():
    As = 10
    Bs = 12
    Cs = 14
    Ds = 5
    minutes_per_A = 2
    minutes_per_B = 1
    minutes_per_D = -1
    total_extra_recess = As * minutes_per_A + Bs * minutes_per_B + Ds * minutes_per_D
    result = total_extra_recess
    return result

print(solution())