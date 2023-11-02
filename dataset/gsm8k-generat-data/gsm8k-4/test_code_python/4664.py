def solution():
    """Phill had some friends over for pizza. He opens the pizza box and discovers it hasn't been sliced. Phill cuts the pizza in half, and then cuts both halves in half, and then cuts each slice in half again. Phill then passes out 1 slice to 3 of his friends and 2 slices to 2 of his friends. How many slices of pizza are left for Phill?"""
    # Calculate the total number of slices
    total_slices = 2 * 2 * 2 * 2

    # Calculate the number of slices given to Phill's friends
    given_slices = (3 * 1) + (2 * 2)

    # Calculate the number of slices left for Phill
    left_slices = total_slices - given_slices

    result = left_slices
    return result

print(solution())