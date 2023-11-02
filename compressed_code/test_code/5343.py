def solution():
    
    blue_packages = 3
    red_packages = 5
    beads_per_package = 40
    total_blue_beads = blue_packages * beads_per_package
    total_red_beads = red_packages * beads_per_package
    total_beads = total_blue_beads + total_red_beads
    result = total_beads
    return result

print(solution())