def solution():
    """If there are 8 slices in a large pizza, how many slices will remain if Mary orders 2 large pizzas and eats 7 slices?"""
    # Define the number of slices in a large pizza
    SLICES_PER_PIZZA = 8

    # Calculate the total number of slices in 2 large pizzas
    total_slices = 2 * SLICES_PER_PIZZA

    # Subtract the number of slices Mary ate
    remaining_slices = total_slices - 7

    # Display the number of slices remaining
    result = remaining_slices
    return result

print(solution())