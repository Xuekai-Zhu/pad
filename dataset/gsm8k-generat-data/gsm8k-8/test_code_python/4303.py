def solution():
    # Determine the number of roosters based on the number of hens
    num_roosters = 12 / 3

    # Determine the total number of hens and roosters
    total_birds = 12 + num_roosters

    # Determine the total number of chicks
    total_chicks = 12 * 5

    # Determine the total number of chickens
    total_chickens = total_birds + total_chicks
    result = total_chickens
    return result

print(solution())