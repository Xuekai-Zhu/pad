def solution():
    num_burgers = 5
    num_friends = 4

    # Calculate the total number of slices from all burgers
    total_slices = num_burgers * 2

    # Calculate the number of slices given to the first two friends
    num_slices_given = 1 + 2

    # Calculate the number of slices given to the third and fourth friends
    num_slices_given += 3 + 3

    # Calculate the number of slices left for Era
    num_slices_left = total_slices - num_slices_given
    result = num_slices_left
    return result

print(solution())