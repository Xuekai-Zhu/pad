def solution():
    
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