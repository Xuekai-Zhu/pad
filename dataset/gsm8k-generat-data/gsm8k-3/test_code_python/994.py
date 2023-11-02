def solution():
    """Dean ordered 2 large pizzas that were each cut into 12 slices.  His friends Frank and Sammy came over to enjoy some pizza and watch a movie.  Dean was hungry and ate half of the Hawaiian pizza.  Frank only ate 3 slices of Hawaiian pizza and Sammy ate a third of the cheese pizza.  How many total slices were left over?"""
    # Define the number of slices per pizza
    SLICES_PER_PIZZA = 12

    # Define the number of pizzas
    NUM_PIZZAS = 2

    # Calculate the total number of slices
    total_slices = SLICES_PER_PIZZA * NUM_PIZZAS

    # Calculate the number of slices of Hawaiian pizza remaining after Dean ate
    hawaiian_slices = (SLICES_PER_PIZZA // 2) - 3

    # Calculate the number of slices of cheese pizza Sammy ate
    cheese_slices = SLICES_PER_PIZZA // 3

    # Calculate the total number of slices remaining
    remaining_slices = total_slices - hawaiian_slices - cheese_slices

    # Display the total number of slices remaining
    result = remaining_slices
    return result

print(solution())