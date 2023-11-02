def solution():
    # Calculate the height of the tree after 8 years, in feet
    height_in_feet = 52 + 5 * 8  # the tree grows 5 feet every year for 8 years
    # Convert the height to inches
    height_in_inches = height_in_feet * 12  # 1 foot is 12 inches
    result = height_in_inches
    return result

print(solution())