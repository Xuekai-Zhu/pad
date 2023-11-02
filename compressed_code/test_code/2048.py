def solution():
    
    jenson_shirts_per_day = 3
    kingsley_pants_per_day = 5
    fabric_per_shirt = 2
    fabric_per_pants = 5
    total_days = 3
    total_jenson_shirts = jenson_shirts_per_day * total_days
    total_kingsley_pants = kingsley_pants_per_day * total_days
    total_fabric = (total_jenson_shirts * fabric_per_shirt) + (total_kingsley_pants * fabric_per_pants)
    result = total_fabric
    return result

print(solution())