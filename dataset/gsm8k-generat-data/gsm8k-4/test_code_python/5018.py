def solution():
    """A carton contains 12 boxes. If each box has 10 packs of cheese cookies, what's the price of a pack of cheese cookies if a dozen cartons cost $1440?"""
    # Calculate the total number of packs of cheese cookies
    total_packs = 12 * 10 * 12

    # Calculate the price per pack
    price_per_pack = 1440 / total_packs

    # return the result
    result = price_per_pack
    return result

print(solution())