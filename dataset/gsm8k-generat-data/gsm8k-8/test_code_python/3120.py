def solution():
    # Calculate the number of packages in each box
    packages_per_box = 6
    total_packages = packages_per_box * 2

    # Calculate the number of soaps in each package
    soaps_per_package = 192

    # Calculate the total number of soaps in both boxes
    total_soaps = total_packages * soaps_per_package
    result = total_soaps
    return result

print(solution())