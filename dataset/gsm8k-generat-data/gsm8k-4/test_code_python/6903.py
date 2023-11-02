def solution():
    """Hearty bought 3 packages of blue and 5 packages of red. If there are 40 beads in each package, how many beads does Hearty have in all?"""
    # Define the number of packages of blue and red beads
    blue_packages = 3
    red_packages = 5

    # Define the number of beads in each package
    beads_per_package = 40

    # Calculate the total number of beads Hearty has
    total_beads = (blue_packages + red_packages) * beads_per_package

    # return the result
    result = total_beads
    return result

print(solution())