def solution():
    """Alex has 2 cakes that are each cut into 8 slices. A fourth of the slices are given away to his friends. A third of the remaining slices are given away to his family. Alex eats 3 slices. How many slices of the cake are left?"""
    # Define the total number of slices
    total_slices = 2 * 8

    # Calculate the number of slices given away to friends
    friend_slices = total_slices // 4

    # Calculate the number of remaining slices
    remaining_slices = total_slices - friend_slices

    # Calculate the number of slices given away to family
    family_slices = remaining_slices // 3

    # Calculate the number of slices left after Alex eats 3
    slices_left = remaining_slices - family_slices - 3

    # Return the result
    result = slices_left
    return result

print(solution())