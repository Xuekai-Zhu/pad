def solution():
    """When Mark bought his first tv it was was 24 inches wide and 16 inches tall. It cost $672. His new tv is 48 inches wide and 32 inches tall and costs $1152. How much more expensive as measure by cost per square inch, was his first TV compared to his newest TV?"""
    old_tv_width = 24
    old_tv_height = 16
    old_tv_cost = 672
    new_tv_width = 48
    new_tv_height = 32
    new_tv_cost = 1152
    old_tv_area = old_tv_width * old_tv_height
    new_tv_area = new_tv_width * new_tv_height
    old_tv_cost_per_inch = old_tv_cost / old_tv_area
    new_tv_cost_per_inch = new_tv_cost / new_tv_area
    difference = new_tv_cost_per_inch - old_tv_cost_per_inch
    result = difference
    return result

print(solution())