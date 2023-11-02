def solution():
    total_chickens = 440  # Uncle Ben has 440 chickens on his farm
    roosters = 39  # There are 39 roosters on the farm
    hens = total_chickens - roosters  # The rest of the chickens are hens
    non_laying_hens = 15  # 15 of the hens do not lay eggs
    laying_hens = hens - non_laying_hens  # The rest of the hens lay eggs

    # Calculate the total number of eggs that Uncle Ben will have
    total_eggs = laying_hens * 3

    result = total_eggs
    return result

print(solution())