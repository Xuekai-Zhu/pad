def solution():
    first_tv_width = 24
    first_tv_height = 16
    first_tv_cost = 672

    newest_tv_width = 48
    newest_tv_height = 32
    newest_tv_cost = 1152

    # Calculate the area of the first TV
    first_tv_area = first_tv_width * first_tv_height

    # Calculate the area of the newest TV
    newest_tv_area = newest_tv_width * newest_tv_height

    # Calculate the cost per square inch of the first TV
    first_tv_cost_per_inch = first_tv_cost / first_tv_area

    # Calculate the cost per square inch of the newest TV
    newest_tv_cost_per_inch = newest_tv_cost / newest_tv_area

    # Calculate the difference in cost per square inch between the two TVs
    cost_per_inch_difference = newest_tv_cost_per_inch - first_tv_cost_per_inch
    result = cost_per_inch_difference
    return result

print(solution())