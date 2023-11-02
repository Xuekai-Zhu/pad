def solution():
    """Mrs. Fredrickson has 80 chickens where 1/4 are roosters and the rest are hens. Only three-fourths of those hens lay eggs. How many chickens does Mr. Fredrickson have that do not lay eggs?"""
    total_chickens = 80
    roosters = total_chickens / 4
    hens = total_chickens - roosters
    egg_laying_hens = hens * 3/4
    non_egg_laying_chickens = total_chickens - roosters - egg_laying_hens
    result = non_egg_laying_chickens
    return result

print(solution())