def solution():
    """Bob wants to build a pyramid out of legos with 3 levels where the bottom level has 7 legos per side and each level has one less lego per side than the level below it. How many legos total will he need?"""
    bottom_level = 7
    middle_level = bottom_level - 1
    top_level = middle_level - 1
    total_legos = bottom_level**2 + middle_level**2 + top_level**2
    result = total_legos
    return result

print(solution())