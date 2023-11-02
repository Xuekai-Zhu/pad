def solution():
    '''Uncle Ben has 440 chickens on his farm. 39 are roosters and the rest are hens. 15 of his hens
    do not lay eggs, and the rest do. If each egg-laying hen lays 3 eggs, how many eggs will Uncle Ben have?'''
    # Total number of hens
    hens = 440 - 39
    # Number of hens that lay eggs
    laying_hens = hens - 15
    # Total number of eggs laid
    total_eggs = laying_hens * 3
    result = total_eggs
    return result

print(solution())