def solution():
    """Martin eats 1/2 cup of berries every day. The grocery store is selling a package of berries (1 cup per pack) for $2.00. How much will he spend on berries in a 30 day period?"""
    daily_cups = 0.5
    pack_size = 1
    price_per_pack = 2.00
    days = 30
    total_cups = daily_cups * days
    total_packs = total_cups / pack_size
    total_cost = total_packs * price_per_pack
    result = total_cost
    return result

print(solution())