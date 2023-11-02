def solution():
    # Calculate the total number of slices in the burgers
    total_slices = 5 * 2

    # Calculate the number of slices given to the first and second friends
    first_two_slices = 1 + 2

    # Calculate the number of slices given to the third and fourth friends
    third_fourth_slices = 3 + 3

    # Calculate the total number of slices given away
    total_given_slices = first_two_slices + third_fourth_slices

    # Calculate the number of slices left for Era and her friends
    slices_left = total_slices - total_given_slices
    result = slices_left
    return result

print(solution())