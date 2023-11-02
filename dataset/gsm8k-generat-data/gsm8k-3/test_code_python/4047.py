def solution():
    """Marcia needs to add 3 skirts, 2 pairs of pants and 5 blouses to her work wardrobe.  A department store is offering a sale on pants; buy 1 pair get 1 pair 1/2 off.  If her skirts are $20.00 each, the blouses are $15.00 and both pairs of pants are $30.00 each.  How much will she spend on her wardrobe?"""
    # Define the prices of each item
    SKIRT_PRICE = 20
    PANTS_PRICE = 30
    BLOUSE_PRICE = 15

    # Define the number of each item that Marcia needs
    skirts_needed = 3
    pants_needed = 2
    blouses_needed = 5

    # Calculate the total cost of the skirts
    skirt_cost = skirts_needed * SKIRT_PRICE

    # Calculate the total cost of the blouses
    blouse_cost = blouses_needed * BLOUSE_PRICE

    # Calculate the total cost of the pants at full price
    pants_cost_full = pants_needed * PANTS_PRICE

    # Calculate the total cost of the pants on sale
    pants_cost_sale = PANTS_PRICE + (PANTS_PRICE * 0.5)

    # Calculate the total cost of all the items
    total_cost = skirt_cost + blouse_cost + pants_cost_full + pants_cost_sale

    # Display the total cost
    result = total_cost
    return result

print(solution())