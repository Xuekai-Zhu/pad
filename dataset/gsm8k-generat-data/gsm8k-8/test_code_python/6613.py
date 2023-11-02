def solution():
    # Calculate the number of hens
    total_chickens = 325
    roosters = 28
    hens = total_chickens - roosters

    # Calculate the number of non-egg-laying hens
    non_egg_laying_hens = 20

    # Calculate the number of egg-laying hens
    egg_laying_hens = hens - non_egg_laying_hens
    result = egg_laying_hens
    return result

print(solution())