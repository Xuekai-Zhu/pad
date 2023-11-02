def solution():
    """Tom split 2 apples into 8 slices each. Tom gave 3/8ths of the apple slices to his friend Jerry, then ate half of the remaining slices. How many apple slices does Tom have left?"""
    # Define the number of apples and slices per apple
    num_apples = 2
    slices_per_apple = 8

    # Calculate the total number of slices
    total_slices = num_apples * slices_per_apple

    # Calculate the number of slices given to Jerry
    jerry_slices = total_slices * (3/8)

    # Calculate the number of slices remaining after giving some to Jerry
    remaining_slices = total_slices - jerry_slices

    # Calculate the number of slices Tom ate
    tom_slices = remaining_slices * (1/2)

    # Calculate the number of slices left
    slices_left = remaining_slices - tom_slices

    result = slices_left
    return result

print(solution())