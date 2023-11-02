def solution():
    
    total_necklaces = 9 * 8 - 40
    necklaces_per_pack = 8
    packs_opened = total_necklaces // necklaces_per_pack
    result = packs_opened
    return result

print(solution())