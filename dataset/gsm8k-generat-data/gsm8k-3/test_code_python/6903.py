def solution():
    """Hearty bought 3 packages of blue and 5 packages of red. If there are 40 beads in each package, how many beads does Hearty have in all?"""
    # Define the number of packages and beads per package
    BLUE_PACKAGES = 3
    RED_PACKAGES = 5
    BEADS_PER_PACKAGE = 40

    # Calculate the total number of blue beads
    blue_beads = BLUE_PACKAGES * BEADS_PER_PACKAGE

    # Calculate the total number of red beads
    red_beads = RED_PACKAGES * BEADS_PER_PACKAGE

    # Calculate the total number of beads
    total_beads = blue_beads + red_beads

    # Display the total number of beads
    result = total_beads
    return result

print(solution())