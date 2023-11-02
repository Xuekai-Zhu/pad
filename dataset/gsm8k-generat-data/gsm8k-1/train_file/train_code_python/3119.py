def solution():
    """There are 192 soaps in a package. They put them in 2 big boxes. If each box contains 6 packages, how much soap do the 2 boxes contain in total?"""
    soaps_per_package = 192
    packages_per_box = 6
    total_packages = packages_per_box * 2
    total_soaps = total_packages * soaps_per_package
    result = total_soaps
    return result

print(solution())