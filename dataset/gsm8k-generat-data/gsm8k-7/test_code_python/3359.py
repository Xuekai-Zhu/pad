def solution():
    num_brothers = 3
    slices_per_brother = 12
    slices_per_small_pizza = 8
    slices_per_large_pizza = 14
    num_small_pizzas = 1

    # Calculate the total number of slices of pizza needed
    total_slices_needed = num_brothers * slices_per_brother

    # Calculate the number of slices covered by the small pizzas
    slices_from_small_pizzas = num_small_pizzas * slices_per_small_pizza

    # Calculate the number of slices still needed after accounting for small pizzas
    slices_left = total_slices_needed - slices_from_small_pizzas

    # Calculate the number of large pizzas needed to cover the remaining slices
    num_large_pizzas = slices_left / slices_per_large_pizza

    result = num_large_pizzas
    return result

print(solution())