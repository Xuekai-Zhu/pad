def solution():
    
    packs = 15
    red_per_pack = 1
    extra_red_packs = 3
    extra_red_per_pack = 2
    total_red = (packs - extra_red_packs) * red_per_pack + extra_red_packs * (red_per_pack + extra_red_per_pack)
    result = total_red
    return result

print(solution())