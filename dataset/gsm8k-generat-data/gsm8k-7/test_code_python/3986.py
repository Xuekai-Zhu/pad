def solution():
    num_children = 48
    num_sweets_per_child = 4
    left_over = 1/3

    # Calculate the total number of sweets taken by the children
    total_sweets_taken = num_children * num_sweets_per_child

    # Calculate the original number of sweets in the pack
    original_num_sweets = total_sweets_taken / (1 - left_over)

    result = original_num_sweets
    return result

print(solution())