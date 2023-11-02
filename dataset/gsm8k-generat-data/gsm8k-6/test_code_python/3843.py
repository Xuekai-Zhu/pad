def solution():
    # Calculate the total number of slices of the pie
    total_slices = 8

    # Calculate the number of slices given to Joe and Darcy
    slices_given_joe_darcy = (1/2) * total_slices

    # Calculate the number of slices given to Carl
    slices_given_carl = (1/4) * total_slices

    # Calculate the number of slices left
    slices_left = total_slices - slices_given_joe_darcy - slices_given_carl
    result = slices_left
    return result

print(solution())