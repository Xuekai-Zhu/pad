def solution():
    """John and Sam were hungry so they ordered an extra-large pizza that was pre-sliced into 12 pieces.  John ate 3 slices while Sam ate twice the amount that John ate.  How many slices of pizza were left?"""
    # Define the number of slices in the pizza
    pizza_slices = 12

    # Calculate the number of slices John ate
    john_slices = 3

    # Calculate the number of slices Sam ate
    sam_slices = john_slices * 2

    # Calculate the total number of slices eaten
    total_slices = john_slices + sam_slices

    # Calculate the number of slices left
    slices_left = pizza_slices - total_slices

    # Display the number of slices left
    result = slices_left
    return result

print(solution())