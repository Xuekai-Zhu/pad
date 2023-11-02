def solution():
    
    total_chickens = 325
    roosters = 28
    non_laying_hens = 20
    egg_laying_hens = total_chickens - roosters - non_laying_hens
    result = egg_laying_hens
    return result

print(solution())