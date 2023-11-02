def solution():
    num_black_packs = 3
    num_yellow_packs = 3
    black_pack_size = 5
    yellow_pack_size = 2

    # Calculate total number of black shirts
    total_black_shirts = num_black_packs * black_pack_size

    # Calculate total number of yellow shirts 
    total_yellow_shirts = num_yellow_packs * yellow_pack_size

    # Calculate total number of shirts bought
    total_shirts = total_black_shirts + total_yellow_shirts
    result = total_shirts
    return result

print(solution())