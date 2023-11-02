def solution():
    """There are 192 soaps in a package. They put them in 2 big boxes. If each box contains 6 packages, how much soap do the 2 boxes contain in total?"""
    soaps_per_package = 192
    packages_per_box = 6
    boxes = 2
    total_soaps = soaps_per_package * packages_per_box * boxes
    result = total_soaps
    return result

print(solution())