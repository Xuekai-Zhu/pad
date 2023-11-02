def solution():
    bracelet_price = 15
    num_bracelets = 3

    necklace_price = 10
    num_necklaces = 2

    mug_price = 20
    num_mugs = 1

    total_cost = (bracelet_price * num_bracelets) + (necklace_price * num_necklaces) + (mug_price * num_mugs)

    change = 100 - total_cost
    result = change
    return result

print(solution())