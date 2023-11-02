def solution():
    total_slices = 2 * 12  # Stephen ordered 2 large pizzas, each with 12 slices

    # Calculate the number of slices Stephen ate
    stephen_slices = total_slices * 0.25

    # Calculate the number of slices remaining after Stephen ate
    remaining_slices = total_slices - stephen_slices

    # Calculate the number of slices Pete ate
    pete_slices = remaining_slices * 0.5

    # Calculate the number of slices left over
    left_over_slices = remaining_slices - pete_slices
    result = left_over_slices
    return result

print(solution())