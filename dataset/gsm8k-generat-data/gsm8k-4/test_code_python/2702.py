def solution():
    """Stephen ordered 2 large pizzas, both cut into 12 slices. He ate 25% of the pizza. His friend Pete ate 50% of the remaining pizza. How many slices are left over?"""
    # Define the initial number of slices
    initial_slices = 2 * 12

    # Calculate the number of slices Stephen ate
    stephen_slices = initial_slices * 0.25

    # Calculate the number of slices remaining after Stephen ate
    remaining_slices = initial_slices - stephen_slices

    # Calculate the number of slices Pete ate
    pete_slices = remaining_slices * 0.5

    # Calculate the number of slices left over
    leftover_slices = remaining_slices - pete_slices

    # return the result
    result = leftover_slices
    return result

print(solution())