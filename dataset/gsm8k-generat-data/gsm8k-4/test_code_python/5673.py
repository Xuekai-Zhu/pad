def solution():
    """John and Sam were hungry so they ordered an extra-large pizza that was pre-sliced into 12 pieces. John ate 3 slices while Sam ate twice the amount that John ate. How many slices of pizza were left?"""
    # Define the total number of pizza slices
    total_slices = 12

    # Calculate the number of slices John ate
    john_slices = 3

    # Calculate the number of slices Sam ate
    sam_slices = john_slices * 2

    # Calculate the total number of slices eaten
    eaten_slices = john_slices + sam_slices

    # Calculate the number of slices left
    left_slices = total_slices - eaten_slices

    # return the result
    result = left_slices
    return result

print(solution())