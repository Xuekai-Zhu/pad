def solution():
    """A whole pizza was cut into 8 slices. Angeli and Marlon ate 3/2 slices each. How many slices of pizza are left?"""
    # Define the total number of slices in the pizza
    total_slices = 8

    # Calculate the number of slices eaten by Angeli and Marlon together
    eaten_slices = 3/2 + 3/2

    # Calculate the number of slices left
    left_slices = total_slices - eaten_slices

    # Return the result
    result = left_slices
    return result

print(solution())