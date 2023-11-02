def solution():
    # Define the number of blue and red packages purchased
    blue_packages = 3
    red_packages = 5

    # Define the number of beads in each package
    beads_per_package = 40

    # Calculate the total number of beads
    total_beads = (blue_packages + red_packages) * beads_per_package
    result = total_beads
    return result

print(solution())