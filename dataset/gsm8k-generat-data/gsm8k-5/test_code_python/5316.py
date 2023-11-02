def solution():
    bread_slices = 2 * 20  # Shane has 2 packages of sliced bread, each containing 20 slices
    ham_slices = 2 * 8  # Shane has 2 packages of sliced ham, each containing 8 slices

    # Calculate the maximum number of ham sandwiches Shane can make
    max_sandwiches = ham_slices // 2  # Each sandwich uses 2 slices of ham

    # Calculate the number of bread slices required for the maximum number of sandwiches
    required_bread = max_sandwiches * 2  # Each sandwich uses 2 slices of bread

    # Calculate the number of bread slices leftover
    leftover_bread = bread_slices - required_bread
    result = leftover_bread
    return result

print(solution())