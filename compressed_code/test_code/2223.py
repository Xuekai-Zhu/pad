def solution():
    
    white_pack_size = 6
    blue_pack_size = 4
    white_packs = 3
    blue_packs = 2
    white_total = white_pack_size * white_packs
    blue_total = blue_pack_size * blue_packs
    total_tshirts = white_total + blue_total
    result = total_tshirts
    return result

print(solution())