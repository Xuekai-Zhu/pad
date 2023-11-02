def solution():
    
    hens = 12
    roosters = hens // 3
    chicks_per_hen = 5
    total_chicks = hens * chicks_per_hen
    total_chickens = hens + roosters + total_chicks
    result = total_chickens
    return result

print(solution())