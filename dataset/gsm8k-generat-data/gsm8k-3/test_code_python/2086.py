def solution():
    """A jewelry store is restocking its shelves. The necklace stand, which can hold 12 necklaces, currently holds 5 necklaces. The ring display, which can hold 30 rings, currently holds 18 rings. The bracelet display, which can hold 15 bracelets, currently holds 8 bracelets. The store’s supplier charges $4 per necklace, $10 per ring, and $5 per bracelet. How much, in dollars, will the store need to pay to fill the displays?"""

    # Define the capacity and current number of necklaces, rings, and bracelets
    NECKLACE_CAPACITY = 12
    RING_CAPACITY = 30
    BRACELET_CAPACITY = 15
    current_necklaces = 5
    current_rings = 18
    current_bracelets = 8

    # Define the price of each necklace, ring, and bracelet
    NECKLACE_PRICE = 4
    RING_PRICE = 10
    BRACELET_PRICE = 5

    # Calculate the number of missing items for each display
    missing_necklaces = NECKLACE_CAPACITY - current_necklaces
    missing_rings = RING_CAPACITY - current_rings
    missing_bracelets = BRACELET_CAPACITY - current_bracelets

    # Calculate the total cost of filling the displays
    total_cost = missing_necklaces * NECKLACE_PRICE + missing_rings * RING_PRICE + missing_bracelets * BRACELET_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())