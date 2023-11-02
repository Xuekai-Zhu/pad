def solution():
    """A small pizza has 6 slices, a medium pizza has 8 slices whereas a large pizza has 12 slices. How many slices of pizza will you have if you bought a total of 15 pizzas and you know you ordered 4 small pizzas and 5 medium pizzas?"""
    # Define the number of slices per pizza for each size
    SMALL_SLICES = 6
    MEDIUM_SLICES = 8
    LARGE_SLICES = 12

    # Define the number of each size of pizza purchased
    small_pizzas = 4
    medium_pizzas = 5
    large_pizzas = 15 - small_pizzas - medium_pizzas

    # Calculate the total number of slices
    total_slices = (small_pizzas * SMALL_SLICES) + (medium_pizzas * MEDIUM_SLICES) + (large_pizzas * LARGE_SLICES)

    # Display the total number of slices
    result = total_slices
    return result

print(solution())