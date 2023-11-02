def solution():
    # Calculate the total number of slices of burgers
    total_slices = 5 * 2  # 5 burgers, each sliced into 2 halves

    # Calculate the number of slices given to the first and second friends
    first_two = 1 + 2  # first friend gets 1 slice, second friend gets 2 slices

    # Calculate the number of slices given to the third and fourth friends
    third_fourth = 2 * 3  # third and fourth friends each get 3 slices

    # Calculate the number of slices left for Era
    slices_left = total_slices - first_two - third_fourth
    result = slices_left
    return result

print(solution())