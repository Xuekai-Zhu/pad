def solution():
    # Calculate the total number of ham slices
    ham_slices = 2 * 8

    # Calculate the maximum number of sandwiches that can be made with the available ham
    max_sandwiches = ham_slices // 2

    # Calculate the total number of bread slices used for the sandwiches
    bread_slices_used = max_sandwiches * 2

    # Calculate the total number of bread slices remaining
    bread_slices_remaining = (2 * 20) - bread_slices_used
    result = bread_slices_remaining
    return result

print(solution())