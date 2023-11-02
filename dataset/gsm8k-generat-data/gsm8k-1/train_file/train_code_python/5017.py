def solution():
    """A carton contains 12 boxes. If each box has 10 packs of cheese cookies, what's the price of a pack of cheese cookies if a dozen cartons cost $1440?"""
    cartons = 12
    boxes_per_carton = 10
    total_boxes = cartons * boxes_per_carton
    price_per_dozen_cartons = 1440
    price_per_pack = price_per_dozen_cartons / (total_boxes * 12)
    result = price_per_pack
    return result

print(solution())