def solution():
    """Bob wants to build a pyramid out of legos with 3 levels where the bottom level has 7 legos per side and each level has one less lego per side than the level below it. How many legos total will he need?"""
    # Define the number of levels and the legos per side in the bottom level
    levels = 3
    legos_per_side = 7

    # Initialize the total number of legos
    total_legos = 0

    # Iterate through each level and calculate the number of legos
    for i in range(levels):
        legos_in_level = (legos_per_side - i) ** 2
        total_legos += legos_in_level

    # return the result
    result = total_legos
    return result

print(solution())