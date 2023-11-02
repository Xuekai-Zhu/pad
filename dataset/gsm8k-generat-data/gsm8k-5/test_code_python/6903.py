def solution():
    blue_packages = 3  # Hearty bought 3 packages of blue beads
    red_packages = 5  # Hearty bought 5 packages of red beads
    beads_per_package = 40  # Each package contains 40 beads

    # Calculate the total number of blue beads
    total_blue_beads = blue_packages * beads_per_package

    # Calculate the total number of red beads
    total_red_beads = red_packages * beads_per_package

    # Calculate the total number of beads Hearty has in all
    total_beads = total_blue_beads + total_red_beads
    result = total_beads
    return result

print(solution())