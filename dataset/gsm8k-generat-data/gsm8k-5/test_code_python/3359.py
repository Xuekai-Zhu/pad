def solution():
    total_slices_needed = 2 * 12 * 3  # Ben and his two brothers each eat 12 pizza slices
                                     # and there are 3 of them, so they need 72 slices total
    slices_per_small_pizza = 8  # Each small pizza has 8 slices
    slices_per_large_pizza = 14  # Each large pizza has 14 slices

    # Calculate the number of small pizzas needed
    small_pizzas_needed = total_slices_needed // slices_per_small_pizza
    if total_slices_needed % slices_per_small_pizza != 0:
        small_pizzas_needed += 1

    # Calculate the number of large pizzas needed
    large_pizzas_needed = (small_pizzas_needed * slices_per_small_pizza - total_slices_needed) // \
                          slices_per_large_pizza
    if (small_pizzas_needed * slices_per_small_pizza - total_slices_needed) % slices_per_large_pizza != 0:
        large_pizzas_needed += 1

    result = large_pizzas_needed
    return result

print(solution())