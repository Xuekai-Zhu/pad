def solution():
    base_side_length = 7
    total_levels = 3

    # Calculate the total number of legos in the first level
    first_level = base_side_length ** 2

    # Calculate the total number of legos in all levels above the first level
    additional_legos = 0
    for i in range(total_levels - 1):
        additional_legos += (base_side_length - (i+1)) ** 2

    # Calculate the total number of legos in the pyramid
    total_legos = first_level + additional_legos
    result = total_legos
    return result

print(solution())