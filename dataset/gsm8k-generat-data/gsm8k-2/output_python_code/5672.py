def solution():
    """John and Sam were hungry so they ordered an extra-large pizza that was pre-sliced into 12 pieces. John ate 3 slices while Sam ate twice the amount that John ate. How many slices of pizza were left?"""
    total_slices = 12
    john_slices = 3
    sam_slices = 2 * john_slices
    remaining_slices = total_slices - john_slices - sam_slices
    result = remaining_slices
    return result

print(solution())