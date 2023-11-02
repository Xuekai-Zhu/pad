def solution():
    """A small pizza can gives 4 slices, and a large pizza gives 8 slices.  George purchased 3 small and 2 large pizzas.  George would like to eat 3 pieces.  His friend Bob would like to eat one more piece than George.  Susie will eat half as many as Bob.  Bill, Fred and Mark would each like 3 pieces.  How many slices of pizza will be left over?"""
    # Define the number of slices in a small and large pizza
    SMALL_PIZZA_SLICES = 4
    LARGE_PIZZA_SLICES = 8

    # Define the number of small and large pizzas purchased
    num_small_pizzas = 3
    num_large_pizzas = 2

    # Calculate the total number of slices
    total_slices = (num_small_pizzas * SMALL_PIZZA_SLICES) + (num_large_pizzas * LARGE_PIZZA_SLICES)

    # Subtract the slices that George, Bob, and Susie will eat
    remaining_slices = total_slices - 3 - 4 - 2 - 9

    # Display the remaining slices
    result = remaining_slices
    return result

print(solution())