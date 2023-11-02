def solution():
    num_children = 20
    num_pizzas = 5
    slice_options = [6, 8, 10]

    for num_slices in slice_options:
        total_slices = num_pizzas * num_slices
        if total_slices % num_children == 0:
            result = num_slices
            break

    return result

print(solution())