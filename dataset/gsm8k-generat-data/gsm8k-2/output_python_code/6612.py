def solution():
    """Mr. Curtis has 325 chickens on his farm where 28 are roosters and the rest are hens. Twenty hens do not lay eggs while the rest of the hens do. How many egg-laying hens does Mr. Curtis have on his farm?"""
    total_chickens = 325
    roosters = 28
    non_laying_hens = 20
    egg_laying_hens = total_chickens - roosters - non_laying_hens
    result = egg_laying_hens
    return result

print(solution())