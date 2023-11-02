def solution():
    """Albert is wondering how much pizza he can eat in one day. He buys 2 large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8 slices. If he eats it all, how many pieces does he eat that day?"""
    # Define the number of slices in a large pizza and a small pizza
    LARGE_SLICES = 16
    SMALL_SLICES = 8

    # Define the number of large and small pizzas purchased
    num_large_pizzas = 2
    num_small_pizzas = 2

    # Calculate the total number of slices
    total_slices = (num_large_pizzas * LARGE_SLICES) + (num_small_pizzas * SMALL_SLICES)

    # Calculate the number of pieces Albert eats
    pieces_eaten = total_slices

    # Return the result
    result = pieces_eaten
    return result

print(solution())