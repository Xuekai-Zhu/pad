def solution():
    total_chickens = 325
    roosters = 28
    non_egg_laying_hens = 20

    # Calculate the total number of hens on the farm
    total_hens = total_chickens - roosters

    # Calculate the number of egg-laying hens
    egg_laying_hens = total_hens - non_egg_laying_hens
    result = egg_laying_hens
    return result

print(solution())