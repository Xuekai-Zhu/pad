def solution():
    chickens = 80
    roosters = chickens / 4
    hens = chickens - roosters
    laying_hens = (hens / 4) * 3
    non_laying_chickens = hens - laying_hens
    result = non_laying_chickens
    
    return result

print(solution())