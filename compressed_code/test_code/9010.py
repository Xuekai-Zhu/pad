def solution():
    
    black_pack_size = 5
    black_packs = 3
    black_shirts = black_pack_size * black_packs
    
    yellow_pack_size = 2
    yellow_packs = 3
    yellow_shirts = yellow_pack_size * yellow_packs
    
    total_shirts = black_shirts + yellow_shirts
    result = total_shirts
    return result

print(solution())