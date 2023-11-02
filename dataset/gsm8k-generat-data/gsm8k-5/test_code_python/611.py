def solution():
    # Start with 40 evenly spread slices of pepperoni
    num_slices = 40

    # Cut the pizza in half and then each half in half again
    num_slices = num_slices / 4

    # Give one of the slices to Jelly
    num_slices -= 1

    result = num_slices
    return result

print(solution())