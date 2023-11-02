def solution():
    """Tom split 2 apples into 8 slices each. Tom gave 3/8ths of the apple slices to his friend Jerry, then ate half of the remaining slices. How many apple slices does Tom have left?"""
    total_slices = 2 * 8
    jerry_slices = (3/8) * total_slices
    remaining_slices = total_slices - jerry_slices
    tom_slices = remaining_slices / 2
    result = tom_slices
    return result

print(solution())