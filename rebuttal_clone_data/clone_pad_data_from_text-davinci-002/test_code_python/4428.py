def solution():
    leg1 = 1
    leg2 = 2 * leg1
    leg3 = 0.5 * leg1
    leg4 = 2 * (leg1 + leg2 + leg3)
    total_distance = leg1 + leg2 + leg3 + leg4
    result = total_distance
    return result

print(solution())