def solution():
    # Calculate the total number of slices
    total_slices = 2 * 12

    # Calculate the number of slices Stephen ate
    stephen_slices = 0.25 * total_slices

    # Calculate the number of slices remaining after Stephen ate
    remaining_slices1 = total_slices - stephen_slices

    # Calculate the number of slices Pete ate
    pete_slices = 0.5 * remaining_slices1

    # Calculate the number of slices left over
    slices_left_over = remaining_slices1 - pete_slices
    result = slices_left_over
    return result

print(solution())