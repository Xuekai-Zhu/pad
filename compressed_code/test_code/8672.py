def solution():
    
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