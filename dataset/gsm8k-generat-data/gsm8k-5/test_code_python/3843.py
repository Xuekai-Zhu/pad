def solution():
    total_slices = 8  # Nancy bought a pie sliced into 8 pieces
    slices_given = (1/2) * 2 + (1/4)  # Nancy gave 1/2 of the pie to two people, and 1/4 to another

    # Calculate the number of slices left
    slices_left = total_slices - slices_given
    result = slices_left
    return result

print(solution())