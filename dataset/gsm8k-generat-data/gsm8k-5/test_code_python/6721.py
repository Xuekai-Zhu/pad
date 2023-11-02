def solution():
    tree_height_ft = 52  # The height of the tree is 52 feet
    growth_rate_ft = 5  # The tree grows 5 feet each year
    years = 8  # The tree will grow for 8 years

    # Calculate the final height in feet
    final_height_ft = tree_height_ft + (growth_rate_ft * years)

    # Convert the final height from feet to inches
    final_height_inches = final_height_ft * 12

    result = final_height_inches
    return result

print(solution())