def solution():
    """Marcia needs to add 3 skirts, 2 pairs of pants and 5 blouses to her work wardrobe. A department store is offering a sale on pants; buy 1 pair get 1 pair 1/2 off. If her skirts are $20.00 each, the blouses are $15.00 and both pairs of pants are $30.00 each. How much will she spend on her wardrobe?"""
    # Define the prices of skirts, pants, and blouses
    skirt_price = 20
    pants_price = 30
    blouse_price = 15

    # Calculate the total cost of skirts
    skirt_cost = 3 * skirt_price

    # Calculate the total cost of blouses
    blouse_cost = 5 * blouse_price

    # Calculate the cost of one pair of pants at full price
    full_price_pants = 30

    # Calculate the cost of one pair of pants with the sale discount
    sale_price_pants = 30 + (0.5 * 30)

    # Calculate the total cost of pants
    pants_cost = full_price_pants + sale_price_pants

    # Calculate the total cost of Marcia's wardrobe
    total_cost = skirt_cost + blouse_cost + pants_cost

    result = total_cost
    return result

print(solution())