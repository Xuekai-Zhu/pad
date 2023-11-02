def solution():
    num_slices = 12
    breakfast_portion = 1/3
    lunch_portion = 2

    # Calculate number of sliced used for breakfast
    breakfast_slices = num_slices * breakfast_portion

    # Calculate remaining slices after breakfast
    remaining_slices = num_slices - breakfast_slices

    # Calculate remaining slices after lunch
    remaining_slices = remaining_slices - lunch_portion

    result = remaining_slices
    return result

print(solution())