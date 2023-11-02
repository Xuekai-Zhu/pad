def solution():
    packs_per_box = 10  # Each box contains 10 packs of cheese cookies
    boxes_per_carton = 12  # Each carton contains 12 boxes

    # Calculate the total number of packs in a dozen cartons
    packs_per_dozen_cartons = packs_per_box * boxes_per_carton * 12

    # Calculate the price per pack of cheese cookies
    price_per_pack = 1440 / packs_per_dozen_cartons
    result = price_per_pack
    return result

print(solution())