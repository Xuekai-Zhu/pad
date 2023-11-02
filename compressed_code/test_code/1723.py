def solution():
    
    spoons_per_pack = 30 / 3  
    num_packs = 50 / spoons_per_pack
    
    if num_packs % 1 != 0:
        num_packs = num_packs // 1 + 1
    result = num_packs
    return result

print(solution())