def solution():
    # Calculate the total number of slices in both cakes
    total_slices = 2 * 8 

    # Calculate the number of slices given away to friends
    friend_slices = total_slices // 4 

    # Calculate the remaining slices after giving away to friends
    remaining_slices = total_slices - friend_slices 

    # Calculate the number of slices given away to family
    family_slices = remaining_slices // 3 

    # Calculate the number of slices left after giving away to family and eating 3 slices
    slices_left = remaining_slices - family_slices - 3 

    result = slices_left
    return result

print(solution())