def solution():
    # Calculate the total number of packs of cheese cookies in a dozen cartons
    total_packs = 12 * 12 * 10  # 12 cartons in a dozen, 12 boxes in each carton, 10 packs in each box

    # Calculate the price of a pack of cheese cookies
    price_per_pack = 1440 / total_packs
    result = price_per_pack
    return result

print(solution())