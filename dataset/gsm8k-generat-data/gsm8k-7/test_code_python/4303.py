def solution():
    num_hens = 12
    num_roosters = num_hens // 3  # integer division to only get whole number of roosters
    num_chicks_per_hen = 5

    # Calculate the total number of chicks from all hens
    total_chicks = num_hens * num_chicks_per_hen

    # Add the number of roosters and hens to get the total number of chickens
    total_chickens = num_hens + num_roosters

    # Add the total number of chicks to get the final answer
    total_chickens += total_chicks
    result = total_chickens
    return result

print(solution())