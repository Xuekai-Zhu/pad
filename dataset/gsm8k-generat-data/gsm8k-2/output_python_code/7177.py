def solution():
    """When Mark bought his first tv it was was 24 inches wide and 16 inches tall. It cost $672. His new tv is 48 inches wide and 32 inches tall and costs $1152. How much more expensive as measure by cost per square inch, was his first TV compared to his newest TV?"""
    first_tv_cost = 672
    first_tv_width = 24
    first_tv_height = 16
    first_tv_area = first_tv_width * first_tv_height

    new_tv_cost = 1152
    new_tv_width = 48
    new_tv_height = 32
    new_tv_area = new_tv_width * new_tv_height

    first_tv_cost_per_inch = first_tv_cost / first_tv_area
    new_tv_cost_per_inch = new_tv_cost / new_tv_area

    difference = new_tv_cost_per_inch - first_tv_cost_per_inch
    result = difference

    return result

print(solution())