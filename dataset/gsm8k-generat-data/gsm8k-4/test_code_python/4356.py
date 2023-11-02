def solution():
    """A small pizza has 6 slices, a medium pizza has 8 slices whereas a large pizza has 12 slices. How many slices of pizza will you have if you bought a total of 15 pizzas and you know you ordered 4 small pizzas and 5 medium pizzas?"""
    # Define the number of slices in each type of pizza
    small_slices = 6
    medium_slices = 8
    large_slices = 12

    # Define the number of each type of pizza ordered
    small_pizzas = 4
    medium_pizzas = 5
    large_pizzas = 15 - small_pizzas - medium_pizzas

    # Calculate the total number of slices
    total_slices = (small_pizzas * small_slices) + (medium_pizzas * medium_slices) + (large_pizzas * large_slices)

    # return the result
    result = total_slices
    return result

print(solution())