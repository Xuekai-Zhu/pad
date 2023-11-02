def solution():
    num_pizzas = 2
    slices_per_pizza = 6

    # Calculate the total number of slices of pizza
    total_slices = num_pizzas * slices_per_pizza

    # Calculate the number of slices James ate
    james_slices = total_slices * (2/3)

    result = james_slices
    return result

print(solution())