def solution():
    cartons = 12
    boxes = 10
    packs = 10
    cost = 1440
    pack_price = cost / (cartons * boxes * packs)
    result = pack_price
    return result

print(solution())