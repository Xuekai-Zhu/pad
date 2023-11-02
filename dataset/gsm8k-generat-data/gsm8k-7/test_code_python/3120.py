def solution():
    num_soaps_per_package = 192
    num_packages_per_box = 6
    num_boxes = 2

    # Calculate the total number of soap packages in the two boxes
    total_packages = num_packages_per_box * num_boxes

    # Calculate the total number of soaps in the two boxes
    total_soaps = total_packages * num_soaps_per_package
    result = total_soaps
    return result

print(solution())