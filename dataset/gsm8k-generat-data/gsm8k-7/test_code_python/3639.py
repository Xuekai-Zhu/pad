def solution():
    small_pizza_slices = 4
    large_pizza_slices = 8

    num_small_pizzas = 3
    num_large_pizzas = 2

    num_george_slices = 3
    num_bob_slices = num_george_slices + 1
    num_susie_slices = num_bob_slices / 2
    num_others_slices = 3 * 3

    # Calculate the total number of slices of pizza
    total_slices = (num_small_pizzas * small_pizza_slices) + (num_large_pizzas * large_pizza_slices)

    # Subtract the slices eaten by each person
    total_slices -= (num_george_slices + num_bob_slices + num_susie_slices + num_others_slices)

    result = total_slices
    return result

print(solution())