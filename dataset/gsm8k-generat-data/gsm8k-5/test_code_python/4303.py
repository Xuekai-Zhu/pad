def solution():
    # Calculate the number of roosters
    num_roosters = 12 // 3  # For every 3 hens, there is 1 rooster

    # Calculate the number of chicks per hen
    num_chicks_per_hen = 5

    # Calculate the total number of hens and chicks
    total_hens_and_chicks = 12 + (12 * num_chicks_per_hen)

    # Calculate the total number of roosters and their chicks
    total_roosters_and_chicks = num_roosters + (num_roosters * num_chicks_per_hen)

    # Calculate the total number of chickens
    total_chickens = total_hens_and_chicks + total_roosters_and_chicks
    result = total_chickens
    return result

print(solution())