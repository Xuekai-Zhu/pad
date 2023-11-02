def solution():
    
    white_pack_size = 5
    blue_pack_size = 3
    shirt_cost = 3
    white_packs = 2
    blue_packs = 4
    total_white_shirts = white_pack_size * white_packs
    total_blue_shirts = blue_pack_size * blue_packs
    total_shirts = total_white_shirts + total_blue_shirts
    total_cost = total_shirts * shirt_cost
    result = total_cost
    return result

print(solution())