def solution():
    # Define the number of slices each pizza gives
    small_pizza_slices = 4
    large_pizza_slices = 8

    # Calculate the total number of slices of pizza George bought
    num_small_pizzas = 3
    num_large_pizzas = 2
    total_slices = num_small_pizzas * small_pizza_slices + num_large_pizzas * large_pizza_slices

    # Determine how many slices each person wants
    george_slices = 3
    bob_slices = george_slices + 1
    susie_slices = bob_slices / 2
    bill_slices = 3
    fred_slices = 3
    mark_slices = 3
    total_slices_wanted = george_slices + bob_slices + susie_slices + bill_slices + fred_slices + mark_slices

    # Calculate the number of slices left over
    slices_leftover = total_slices - total_slices_wanted
    result = slices_leftover
    return result

print(solution())