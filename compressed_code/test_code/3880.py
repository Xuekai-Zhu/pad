def solution():
    
    cartons = 12
    boxes_per_carton = 12
    packs_per_box = 10
    total_packs = cartons * boxes_per_carton * packs_per_box
    dozen_price = 1440
    price_per_pack = dozen_price / total_packs
    result = price_per_pack
    return result

print(solution())