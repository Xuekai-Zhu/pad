def solution():
    """Mandy bought 3 packs of black shirts and 3 packs of yellow shirts for her tennis team. The black shirts come in packs of 5, and the yellow shirts come in packs of 2. How many shirts did Mandy buy in all?"""
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