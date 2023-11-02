def solution():
    
    bananas_per_loaf = 4
    monday_loaves = 3
    tuesday_loaves = 2 * monday_loaves
    total_loaves = monday_loaves + tuesday_loaves
    total_bananas = bananas_per_loaf * total_loaves
    result = total_bananas
    return result

print(solution())