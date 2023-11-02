def solution():
    # Calculate the number of roosters and hens on the farm
    num_roosters = 12 // 3  # For every 3 hens, there is 1 rooster
    num_hens = 12

    # Calculate the total number of chicks
    total_chicks = num_hens * 5  # Each hen has 5 chicks

    # Calculate the total number of chickens on the farm
    total_chickens = num_roosters + num_hens + total_chicks
    result = total_chickens
    return result

print(solution())