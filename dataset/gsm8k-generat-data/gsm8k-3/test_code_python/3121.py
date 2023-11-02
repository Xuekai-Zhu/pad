def solution():
    """A whole pizza was cut into 8 slices. Angeli and Marlon ate 3/2 slices each. How many slices of pizza are left?"""
    # Define the number of slices in a whole pizza
    pizza_slices = 8

    # Calculate the number of slices eaten by Angeli and Marlon
    slices_eaten = 3/2 + 3/2

    # Calculate the number of slices left
    slices_left = pizza_slices - slices_eaten

    # Display the number of slices left
    result = slices_left
    return result

print(solution())