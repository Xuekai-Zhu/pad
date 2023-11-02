def solution():
    
    seeds_per_flower = 2
    total_seeds_needed = seeds_per_flower * 20
    seeds_per_pack = 25
    packs_needed = (total_seeds_needed // seeds_per_pack) + 1
    pack_price = 5
    total_price = packs_needed * pack_price
    result = total_price
    return result

print(solution())