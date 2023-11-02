def solution():
    num_blue_packages = 3
    num_red_packages = 5
    beads_per_package = 40

    # Calculate the total number of blue beads
    total_blue_beads = num_blue_packages * beads_per_package

    # Calculate the total number of red beads
    total_red_beads = num_red_packages * beads_per_package

    # Calculate the total number of beads
    total_beads = total_blue_beads + total_red_beads
    result = total_beads
    return result

print(solution())