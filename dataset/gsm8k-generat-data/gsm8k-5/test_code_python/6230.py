def solution():
    total_slices = 2 * 8  # Tom started with 2 apples, split into 8 slices each
    jerry_slices = (3/8) * total_slices  # Tom gave 3/8ths of the slices to Jerry
    remaining_slices = total_slices - jerry_slices  # Tom has this many slices left

    # Tom ate half of the remaining slices
    remaining_slices = remaining_slices / 2

    result = remaining_slices
    return result

print(solution())