def solution():
    """Dave bought 3 packs of white T-shirts and 2 packs of blue T-shirts for his basketball team. The white T-shirts come in packs of 6, and the blue T-shirts come in packs of 4. How many T-shirts did Dave buy in all?"""
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