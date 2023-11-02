def solution():
    # Number of legos for each level
    level1 = 7  # Bottom level has 7 legos per side
    level2 = 6
    level3 = 5

    # Calculate the total number of legos
    total_legos = (level1 ** 2) + (level2 ** 2) + (level3 ** 2)

    result = total_legos
    return result

print(solution())