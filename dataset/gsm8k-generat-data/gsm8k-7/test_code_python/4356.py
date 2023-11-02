def solution():
    num_small_pizzas = 4
    num_medium_pizzas = 5
    num_large_pizzas = 15 - num_small_pizzas - num_medium_pizzas

    num_slices_small = num_small_pizzas * 6
    num_slices_medium = num_medium_pizzas * 8
    num_slices_large = num_large_pizzas * 12

    total_slices = num_slices_small + num_slices_medium + num_slices_large
    result = total_slices
    return result

print(solution())