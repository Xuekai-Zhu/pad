def solution():
    # Calculate the area of the first TV
    area_1 = 24 * 16

    # Calculate the area of the new TV
    area_2 = 48 * 32

    # Calculate the cost per square inch of the first TV
    cost_per_square_inch_1 = 672 / area_1

    # Calculate the cost per square inch of the new TV
    cost_per_square_inch_2 = 1152 / area_2

    # Calculate the difference in cost per square inch
    cost_difference = cost_per_square_inch_2 - cost_per_square_inch_1
    result = cost_difference
    return result

print(solution())