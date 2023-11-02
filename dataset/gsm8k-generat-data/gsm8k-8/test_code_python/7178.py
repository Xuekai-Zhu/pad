def solution():
    # Calculate the area and cost per square inch of the first TV
    area1 = 24 * 16
    cost_per_sq_inch1 = 672 / area1

    # Calculate the area and cost per square inch of the newest TV
    area2 = 48 * 32
    cost_per_sq_inch2 = 1152 / area2

    # Calculate the difference in cost per square inch
    difference = cost_per_sq_inch1 - cost_per_sq_inch2
    result = difference
    return result

print(solution())