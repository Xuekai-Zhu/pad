def solution():
    # Calculate the total number of slices that all three brothers can eat
    total_slices = 3 * 12

    # Calculate the number of slices in the small pizza
    small_slices = 8

    # Calculate the number of slices that need to come from large pizzas
    large_slices_needed = total_slices - small_slices

    # Calculate the number of large pizzas needed
    large_pizzas_needed = large_slices_needed // 14 + (large_slices_needed % 14 > 0)

    result = large_pizzas_needed
    return result

print(solution())