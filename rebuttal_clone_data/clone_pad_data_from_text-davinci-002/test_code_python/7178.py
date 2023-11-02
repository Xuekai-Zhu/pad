def solution():
    cost_1 = 672
    width_1 = 24
    height_1 = 16
    area_1 = width_1 * height_1
    cost_per_square_inch_1 = cost_1 / area_1

    cost_2 = 1152
    width_2 = 48
    height_2 = 32
    area_2 = width_2 * height_2
    cost_per_square_inch_2 = cost_2 / area_2

    result = cost_per_square_inch_1 - cost_per_square_inch_2
    return result

print(solution())