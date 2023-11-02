def solution():
    """Bob wants to build a pyramid out of legos with 3 levels where the bottom level has 7 legos per side and each level has one less lego per side than the level below it. How many legos total will he need?"""
    # Define the number of legos on the bottom level
    legos_per_side = 7

    # Calculate the total number of legos needed for each level
    level1_legos = legos_per_side ** 2
    level2_legos = (legos_per_side - 1) ** 2
    level3_legos = (legos_per_side - 2) ** 2

    # Calculate the total number of legos needed for the pyramid
    total_legos = level1_legos + level2_legos + level3_legos

    # Display the total number of legos needed
    result = total_legos
    return result

print(solution())