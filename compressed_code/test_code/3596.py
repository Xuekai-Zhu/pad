def solution():
    
    total_packs = 15
    red_pencils_per_pack = 1
    extra_red_packs = 3
    extra_red_pencils = 2
    total_red_pencils = total_packs * red_pencils_per_pack + extra_red_packs * extra_red_pencils
    result = total_red_pencils
    return result

print(solution())