def solution():
    small_pizza_slices = 4  # A small pizza has 4 slices
    large_pizza_slices = 8  # A large pizza has 8 slices
    num_small_pizzas = 3  # George purchased 3 small pizzas
    num_large_pizzas = 2  # George purchased 2 large pizzas
    total_slices = (small_pizza_slices * num_small_pizzas) + (large_pizza_slices * num_large_pizzas)  # Total number of slices

    # Calculate the number of slices each person wants to eat
    george_slices = 3
    bob_slices = george_slices + 1
    susie_slices = bob_slices / 2
    bill_slices = 3
    fred_slices = 3
    mark_slices = 3

    # Calculate the total number of slices needed
    total_slices_needed = george_slices + bob_slices + susie_slices + bill_slices + fred_slices + mark_slices

    # Calculate the number of slices left over
    leftover_slices = total_slices - total_slices_needed
    result = leftover_slices
    return result

print(solution())