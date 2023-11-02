def solution():
    """Marcia needs to add 3 skirts, 2 pairs of pants and 5 blouses to her work wardrobe. A department store is offering a sale on pants; buy 1 pair get 1 pair 1/2 off. If her skirts are $20.00 each, the blouses are $15.00 and both pairs of pants are $30.00 each. How much will she spend on her wardrobe?"""
    skirt_cost = 20
    pants_cost = 30
    blouse_cost = 15

    # Calculate total cost of skirts, pants, and blouses before discount
    total_cost = 3*skirt_cost + 2*pants_cost + 5*blouse_cost

    # Apply discount to one pair of pants
    total_cost -= 0.5*pants_cost

    # Calculate final cost with discount
    final_cost = total_cost - pants_cost

    result = final_cost
    return result

print(solution())