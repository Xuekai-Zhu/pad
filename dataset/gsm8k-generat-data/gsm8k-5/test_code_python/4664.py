def solution():
    # Calculate the total number of slices in the pizza
    half = 1
    quarter = 2
    eighth = 4

    total_slices = half + quarter + quarter + eighth + eighth + eighth + eighth

    # Calculate the slices given to Phill's friends
    slices_given = (3 * 1) + (2 * 2)

    # Calculate the remaining slices for Phill
    remaining_slices = total_slices - slices_given
    result = remaining_slices
    return result

print(solution())