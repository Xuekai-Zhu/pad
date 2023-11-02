def solution():
    ratio_1 = 1.5
    ratio_2 = 3
    weight_1 = 600 / ratio_2
    weight_2 = weight_1 / 2
    lift_1 = weight_2 * ratio_1
    lift_2 = weight_1 * ratio_2
    result = lift_1 + lift_2
    return result

print(solution())