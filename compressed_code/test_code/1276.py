def solution():
    
    bracelet_price = 15
    necklace_price = 10
    mug_price = 20
    num_bracelets = 3
    num_necklaces = 2
    num_mugs = 1
    total_price = (bracelet_price * num_bracelets) + (necklace_price * num_necklaces) + (mug_price * num_mugs)
    change = 100 - total_price
    result = change
    return result

print(solution())