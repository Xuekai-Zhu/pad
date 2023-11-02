def solution():
    total_chickens = 440
    num_roosters = 39
    num_hens = total_chickens - num_roosters

    # Calculate the number of egg-laying hens
    num_egg_laying_hens = num_hens - 15

    # Calculate the total number of eggs laid by all egg-laying hens
    total_num_eggs = num_egg_laying_hens * 3
    result = total_num_eggs
    return result

print(solution())