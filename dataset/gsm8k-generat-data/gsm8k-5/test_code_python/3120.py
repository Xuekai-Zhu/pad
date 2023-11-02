def solution():
    soaps_per_package = 192  # There are 192 soaps in a package
    packages_per_box = 6  # Each box contains 6 packages
    boxes = 2  # There are 2 big boxes

    # Calculate the total number of soaps in the 2 boxes
    total_soaps = soaps_per_package * packages_per_box * boxes
    result = total_soaps
    return result

print(solution())