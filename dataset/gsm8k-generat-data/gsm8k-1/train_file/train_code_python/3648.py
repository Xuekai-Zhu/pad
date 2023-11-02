def solution():
    """Uncle Ben has 440 chickens on his farm. 39 are roosters and the rest are hens. 15 of his hens do not lay eggs, and the rest do.
    If each egg-laying hen lays 3 eggs, how many eggs will Uncle Ben have?"""
    total_chickens = 440
    roosters = 39
    hens = total_chickens - roosters
    non_egg_laying_hens = 15
    egg_laying_hens = hens - non_egg_laying_hens
    eggs_per_hen = 3
    total_eggs = egg_laying_hens * eggs_per_hen
    result = total_eggs
    return result

print(solution())