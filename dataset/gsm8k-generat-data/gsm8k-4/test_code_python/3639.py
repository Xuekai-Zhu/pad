def solution():
    """A small pizza can gives 4 slices, and a large pizza gives 8 slices.  George purchased 3 small and 2 large pizzas.  George would like to eat 3 pieces.  His friend Bob would like to eat one more piece than George.  Susie will eat half as many as Bob.  Bill, Fred and Mark would each like 3 pieces.  How many slices of pizza will be left over?"""
    # Calculate the total number of slices of pizza
    small_pizza_slices = 3 * 4
    large_pizza_slices = 2 * 8
    total_slices = small_pizza_slices + large_pizza_slices

    # Calculate the number of slices eaten by George, Bob, and Susie
    george_slices = 3
    bob_slices = george_slices + 1
    susie_slices = bob_slices / 2

    # Calculate the number of slices eaten by Bill, Fred, and Mark
    other_slices = 3 * 3

    # Calculate the total number of slices eaten
    total_eaten = george_slices + bob_slices + susie_slices + other_slices

    # Calculate the number of slices left over
    slices_left = total_slices - total_eaten

    # return the result
    result = slices_left
    return result

print(solution())