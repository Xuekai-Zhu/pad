def solution():
    """Nancy bought a pie sliced it into 8 pieces. She gave 1/2 to Joe and Darcy, and she gave 1/4 to Carl. How many slices were left?"""
    # Define the initial number of pie slices
    pie_slices = 8

    # Calculate the number of slices given to Joe and Darcy
    joe_darcy_slices = pie_slices * (1/2)

    # Calculate the number of slices given to Carl
    carl_slices = pie_slices * (1/4)

    # Calculate the number of slices left
    slices_left = pie_slices - joe_darcy_slices - carl_slices

    result = slices_left
    return result

print(solution())