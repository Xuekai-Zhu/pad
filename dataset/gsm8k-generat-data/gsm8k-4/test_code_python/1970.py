def solution():
    """A family bought 1 box of pizza that is cut into 16 slices. Only three-fourths of the pizza was eaten by the family. How many slices of pizza were left?"""
    # Define the initial number of pizza slices
    initial_slices = 16

    # Calculate the number of pizza slices eaten by the family
    eaten_slices = initial_slices * 3/4

    # Calculate the number of pizza slices left
    left_slices = initial_slices - eaten_slices

    # Return the result
    result = left_slices
    return result

print(solution())