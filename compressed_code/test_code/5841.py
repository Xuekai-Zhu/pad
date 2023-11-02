def solution():
    
    total_people = 13 + 3 + 2
    pouches_per_pack = 6
    total_packs = (total_people // pouches_per_pack) + (total_people % pouches_per_pack > 0)
    result = total_packs
    return result

print(solution())