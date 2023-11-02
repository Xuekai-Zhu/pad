def solution():
    # Calculate the total number of ham slices Shane has
    total_ham_slices = 2 * 8  # buys 2 packages of sliced ham containing 8 slices each

    # Calculate the maximum number of sandwiches Shane can make with the ham he has
    max_sandwiches = total_ham_slices // 2  # each sandwich requires 2 slices of ham

    # Calculate the total number of bread slices needed for the maximum number of sandwiches
    total_bread_slices = max_sandwiches * 2  # each sandwich requires 2 slices of bread

    # Calculate the number of bread slices leftover
    leftover_bread_slices = (2 * 20) - total_bread_slices  # buys 2 packages of sliced bread containing 20 slices each

    result = leftover_bread_slices
    return result

print(solution())