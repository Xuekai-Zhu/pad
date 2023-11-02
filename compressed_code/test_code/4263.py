def solution():
    
    brownies = 30 * 12
    cookies = 20 * 24
    donuts = 15 * 12
    total_items = brownies + cookies + donuts
    price_per_item = 2
    total_fundraiser = total_items * price_per_item
    result = total_fundraiser
    return result

print(solution())