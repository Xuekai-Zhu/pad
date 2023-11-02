def solution():
    num_bread_packages = 2
    slices_per_bread_package = 20
    num_ham_packages = 2
    slices_per_ham_package = 8

    # Calculate the total number of slices of bread
    total_bread_slices = num_bread_packages * slices_per_bread_package

    # Calculate the total number of sandwiches that can be made
    total_sandwiches = num_ham_packages * slices_per_ham_package

    # Calculate the total number of bread slices used for sandwiches
    total_bread_used = total_sandwiches * 2

    # Calculate the number of bread slices leftover
    bread_slices_leftover = total_bread_slices - total_bread_used
    result = bread_slices_leftover
    return result

print(solution())