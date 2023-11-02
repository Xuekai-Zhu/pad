def solution():
    # Calculate the total number of slices each brother can eat
    total_slices = 12 + 12 + 12  # each brother can eat 12 slices

    # Calculate the number of slices from the small pizza
    small_pizza_slices = 8

    # Calculate the number of slices needed from the large pizzas
    remaining_slices = total_slices - small_pizza_slices
    large_pizza_slices = 14
    large_pizzas_needed = remaining_slices // large_pizza_slices
    if remaining_slices % large_pizza_slices != 0:
        large_pizzas_needed += 1

    result = large_pizzas_needed
    return result

print(solution())