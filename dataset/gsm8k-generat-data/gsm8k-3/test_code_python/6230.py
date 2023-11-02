def solution():
    """Tom split 2 apples into 8 slices each. Tom gave 3/8ths of the apple slices to his friend Jerry, then ate half of the remaining slices. How many apple slices does Tom have left?"""
    # Define the number of apples and slices per apple
    APPLES = 2
    SLICES_PER_APPLE = 8

    # Calculate the total number of slices
    total_slices = APPLES * SLICES_PER_APPLE

    # Calculate how many slices Tom gave to Jerry
    jerry_slices = total_slices * (3/8)

    # Calculate how many slices Tom had left
    remaining_slices = total_slices - jerry_slices

    # Calculate how many slices Tom ate
    tom_slices = remaining_slices / 2

    # Calculate how many slices Tom has left
    tom_slices_left = remaining_slices - tom_slices

    # Display the number of slices Tom has left
    result = tom_slices_left
    return result

print(solution())