def solution():
    # Calculate the area and cost per square inch of Mark's first TV
    area_first_tv = 24 * 16
    cost_per_square_inch_first_tv = 672 / area_first_tv

    # Calculate the area and cost per square inch of Mark's newest TV
    area_newest_tv = 48 * 32
    cost_per_square_inch_newest_tv = 1152 / area_newest_tv

    # Calculate the difference in cost per square inch between the two TVs
    difference = cost_per_square_inch_newest_tv - cost_per_square_inch_first_tv
    result = difference
    return result

print(solution())