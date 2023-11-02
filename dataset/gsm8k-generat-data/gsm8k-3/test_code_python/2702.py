def solution():
    """Stephen ordered 2 large pizzas, both cut into 12 slices.  He ate 25% of the pizza.  His friend Pete ate 50% of the remaining pizza.  How many slices are left over?"""
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 12

    # Calculate the total number of slices
    total_slices = 2 * SLICES_PER_PIZZA

    # Calculate the number of slices Stephen ate
    stephen_slices = total_slices * 0.25

    # Calculate the number of slices remaining after Stephen ate
    remaining_slices = total_slices - stephen_slices

    # Calculate the number of slices Pete ate
    pete_slices = remaining_slices * 0.5

    # Calculate the number of slices left over
    left_over_slices = remaining_slices - pete_slices

    # Display the number of slices left over
    result = left_over_slices
    return result

print(solution())