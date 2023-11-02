def solution():
    juice_per_lime = 1/16  # 1 tablespoon per lime
    desired_juice = 1/4 * 2  # double the amount of juice in the recipe
    num_limes_needed = desired_juice / juice_per_lime
    result = num_limes_needed
    return result

print(solution())