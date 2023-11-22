def solution():
    
    # Define the number of slices per apple
    LARGE_SLICES = 5
    SMALL_SLICES = 3

    # Define the number of slices Adam has already consumed
    slices_consumed = 15

    # Calculate the total number of slices Adam has consumed
    slices_consumed = (3 * LARGE_SLICES) + (5 * SMALL_SLICES)

    # Calculate the number of slices left after Adam eats 15
    slices_left = slices_consumed - slices_consumed

    # Display the number of slices left
    result = slices_left
    return result

print(solution())