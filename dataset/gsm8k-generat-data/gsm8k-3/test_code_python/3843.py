def solution():
    """Nancy bought a pie sliced it into 8 pieces. She gave 1/2 to Joe and Darcy, and she gave 1/4 to Carl. How many slices were left?"""
    # Define the number of initial pie slices
    initial_slices = 8

    # Define the fractions given to Joe, Darcy, and Carl
    joe_darcy_fraction = 1/2
    carl_fraction = 1/4

    # Calculate the total slices given to Joe and Darcy
    joe_darcy_slices = initial_slices * joe_darcy_fraction

    # Calculate the total slices given to Carl
    carl_slices = initial_slices * carl_fraction

    # Calculate the remaining slices
    remaining_slices = initial_slices - joe_darcy_slices - carl_slices

    # Display the remaining slices
    result = remaining_slices
    return result

print(solution())