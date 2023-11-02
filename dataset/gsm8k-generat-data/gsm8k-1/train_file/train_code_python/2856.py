def solution():
    """Dave bought 3 packs of white T-shirts and 2 packs of blue T-shirts for his basketball team. The white T-shirts come in packs of 6, and the blue T-shirts come in packs of 4. How many T-shirts did Dave buy in all?"""
    white_packs = 3
    blue_packs = 2
    white_per_pack = 6
    blue_per_pack = 4
    total_white = white_packs * white_per_pack
    total_blue = blue_packs * blue_per_pack
    total_shirts = total_white + total_blue
    result = total_shirts
    return result

print(solution())