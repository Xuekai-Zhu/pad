def solution():
    """There are 192 soaps in a package. They put them in 2 big boxes. If each box contains 6 packages, how much soap do the 2 boxes contain in total?"""
    # Define the number of soaps in a package
    SOAPS_PER_PACKAGE = 192

    # Define the number of packages in a box
    PACKAGES_PER_BOX = 6

    # Calculate the number of soaps in one box
    soaps_per_box = SOAPS_PER_PACKAGE * PACKAGES_PER_BOX

    # Calculate the number of soaps in two boxes
    total_soaps = soaps_per_box * 2

    # Display the total number of soaps
    result = total_soaps
    return result

print(solution())