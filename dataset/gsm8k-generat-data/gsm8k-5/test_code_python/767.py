def solution():
    # Number of kids who went tubing
    tubing_kids = 40 / 4

    # Number of kids who went rafting (half of the tubers)
    rafting_kids = tubing_kids / 2

    # Number of kids who joined both excursions (common to both sets)
    common_kids = tubing_kids - rafting_kids

    result = common_kids
    return result

print(solution())