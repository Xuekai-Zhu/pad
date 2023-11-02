def solution():
    """There are 192 soaps in a package. They put them in 2 big boxes. If each box contains 6 packages, how much soap do the 2 boxes contain in total?"""
    # Define the number of soaps in a package
    soaps_per_package = 192

    # Calculate the number of soaps in a box
    soaps_per_box = soaps_per_package * 6

    # Calculate the total number of soaps in 2 boxes
    total_soaps = soaps_per_box * 2

    # return the result
    result = total_soaps
    return result

print(solution())