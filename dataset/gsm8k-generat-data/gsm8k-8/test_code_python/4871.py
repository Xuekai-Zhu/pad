def solution():
    # Calculate the number of roosters
    num_roosters = 80 * (1/4)

    # Calculate the number of hens
    num_hens = 80 - num_roosters

    # Calculate the number of hens that lay eggs
    num_laying_hens = num_hens * (3/4)

    # Calculate the number of chickens that do not lay eggs
    num_nonlaying_chickens = num_roosters + (num_hens - num_laying_hens)

    result = num_nonlaying_chickens
    return result

print(solution())