def solution():
    # Define the total number of slices
    total_slices = 16

    # Calculate the number of slices eaten during dinner
    dinner_slices = total_slices / 4

    # Calculate the number of slices left after dinner
    remaining_slices1 = total_slices - dinner_slices

    # Calculate the number of slices Yves ate the next day
    yves_slices = remaining_slices1 / 4

    # Calculate the number of slices left after Yves ate
    remaining_slices2 = remaining_slices1 - yves_slices

    # Calculate the number of slices his siblings ate
    sibling_slices = 2 * 2

    # Calculate the total number of slices left
    total_slices_left = remaining_slices2 - sibling_slices
    result = total_slices_left
    return result

print(solution())