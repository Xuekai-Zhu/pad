def solution():
    total_chickens = 325
    roosters = 28
    non_egg_hens = 20
    # Calculate the number of non-rooster chickens
    non_rooster_chickens = total_chickens - roosters
    # Calculate the number of egg-laying hens
    egg_laying_hens = non_rooster_chickens - non_egg_hens
    result = egg_laying_hens
    return result

print(solution())