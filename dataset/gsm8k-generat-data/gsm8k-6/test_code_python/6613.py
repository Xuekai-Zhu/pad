def solution():
    # Find the number of hens on the farm
    hens = 325 - 28  # 28 are roosters, so the rest are hens
    
    # Find the number of egg-laying hens
    egg_laying_hens = hens - 20  # 20 hens do not lay eggs
    
    result = egg_laying_hens
    return result

print(solution())