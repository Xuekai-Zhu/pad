def solution():
    # Calculate the total number of slices before anyone eats
    small_pizza_slices = 4 * 3  # 3 small pizzas, each with 4 slices
    large_pizza_slices = 8 * 2  # 2 large pizzas, each with 8 slices
    total_slices = small_pizza_slices + large_pizza_slices

    # Calculate the number of slices eaten by each person
    george_slices = 3
    bob_slices = george_slices + 1
    susie_slices = bob_slices / 2
    bill_slices = 3
    fred_slices = 3
    mark_slices = 3
    total_slices_eaten = george_slices + bob_slices + susie_slices + bill_slices + fred_slices + mark_slices

    # Calculate the number of slices left over
    slices_left_over = total_slices - total_slices_eaten
    result = slices_left_over
    return result

print(solution())