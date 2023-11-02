def solution():
    """If there are 8 slices in a large pizza, how many slices will remain if Mary orders 2 large pizzas and eats 7 slices?"""
    # Define the number of slices in a large pizza
    slices_per_pizza = 8

    # Calculate the total number of slices in 2 large pizzas
    total_slices = slices_per_pizza * 2

    # Subtract the number of slices Mary eats
    remaining_slices = total_slices - 7

    # Return the result
    result = remaining_slices
    return result

print(solution())