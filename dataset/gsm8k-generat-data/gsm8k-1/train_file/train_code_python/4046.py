def solution():
    """Marcia needs to add 3 skirts, 2 pairs of pants and 5 blouses to her work wardrobe. A department store is offering a sale on pants; buy 1 pair get 1 pair 1/2 off. If her skirts are $20.00 each, the blouses are $15.00 and both pairs of pants are $30.00 each. How much will she spend on her wardrobe?"""
    skirt_price = 20
    pants_price = 30
    blouse_price = 15
    num_skirts = 3
    num_pants = 2
    num_blouses = 5
    sale_pants_discount = pants_price / 2
    total_cost = (skirt_price * num_skirts) + (pants_price * num_pants) + (sale_pants_discount * num_pants) + (blouse_price * num_blouses)
    result = total_cost
    return result

print(solution())