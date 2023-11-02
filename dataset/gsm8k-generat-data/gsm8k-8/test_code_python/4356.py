def solution():
    # Define the number of slices in each size of pizza
    small_slices = 6
    medium_slices = 8
    large_slices = 12

    # Define the number of each size of pizza ordered
    small_pizzas = 4
    medium_pizzas = 5

    # Calculate the total number of slices from the small and medium pizzas
    total_slices = small_slices * small_pizzas + medium_slices * medium_pizzas

    # Calculate the number of slices from the remaining large pizzas
    remaining_pizzas = 15 - small_pizzas - medium_pizzas
    remaining_slices = remaining_pizzas * large_slices

    # Calculate the total number of slices
    total_slices += remaining_slices

    result = total_slices
    return result

print(solution())