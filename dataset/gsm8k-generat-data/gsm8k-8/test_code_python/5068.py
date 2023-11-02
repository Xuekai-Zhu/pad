def solution():
    # Define the variables
    total_slices = 0
    eaten_slices = 6  # Andy ate 3 slices twice
    usable_slices = 0
    pieces_of_toast = 10
    slices_per_toast = 2

    # Calculate the total number of slices
    for i in range(pieces_of_toast):
        usable_slices += slices_per_toast

    # Add the slice that was left over
    usable_slices += 1

    # Subtract the eaten slices
    total_slices = usable_slices + eaten_slices

    result = total_slices
    return result

print(solution())