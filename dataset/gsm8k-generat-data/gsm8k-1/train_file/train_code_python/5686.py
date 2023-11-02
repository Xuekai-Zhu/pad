def solution():
    """Maddie bought 2 packs of white T-shirts and 4 packs of blue T-shirts for her basketball team. The white T-shirts come in packs of 5, and the blue T-shirts come in packs of 3. Each T-shirt cost $3. How much did Maddie spend in all?"""
    white_pack_size = 5
    blue_pack_size = 3
    white_packs = 2
    blue_packs = 4
    price_per_shirt = 3
    total_white_shirts = white_pack_size * white_packs
    total_blue_shirts = blue_pack_size * blue_packs
    total_shirts = total_white_shirts + total_blue_shirts
    total_cost = total_shirts * price_per_shirt
    result = total_cost
    return result

print(solution())