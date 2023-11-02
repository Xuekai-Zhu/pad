def solution():
    # Calculate the number of hens on the farm
    hens = 440 - 39  # total chickens minus roosters
    # Calculate the number of egg-laying hens
    laying_hens = hens - 15  # hens that lay eggs

    # Calculate the total number of eggs that Uncle Ben will have
    total_eggs = laying_hens * 3  # each egg-laying hen lays 3 eggs
    result = total_eggs
    return result

print(solution())