def solution():
    deepest_depth = 2212
    sun_penetration_depth = 1000
    if deepest_depth <= sun_penetration_depth:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())