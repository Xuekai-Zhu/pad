def solution():
    num_small = 4  # You ordered 4 small pizzas
    num_medium = 5  # You ordered 5 medium pizzas
    num_large = 15 - num_small - num_medium  # You bought a total of 15 pizzas, so the remaining pizzas are large

    # Calculate the total number of pizza slices
    total_slices = (num_small * 6) + (num_medium * 8) + (num_large * 12)
    result = total_slices
    return result

print(solution())