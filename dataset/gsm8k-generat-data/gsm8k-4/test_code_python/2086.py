def solution():
    """A jewelry store is restocking its shelves. The necklace stand, which can hold 12 necklaces, currently holds 5 necklaces. The ring display, which can hold 30 rings, currently holds 18 rings. The bracelet display, which can hold 15 bracelets, currently holds 8 bracelets. The store’s supplier charges $4 per necklace, $10 per ring, and $5 per bracelet. How much, in dollars, will the store need to pay to fill the displays?"""
    # Define the number of necklaces, rings, and bracelets needed to fill the displays
    necklaces_needed = 12 - 5
    rings_needed = 30 - 18
    bracelets_needed = 15 - 8

    # Define the prices of necklaces, rings, and bracelets
    necklace_price = 4
    ring_price = 10
    bracelet_price = 5

    # Calculate the total cost of restocking the displays
    total_cost = (necklaces_needed * necklace_price) + (rings_needed * ring_price) + (bracelets_needed * bracelet_price)

    # Return the result
    result = total_cost
    return result

print(solution())