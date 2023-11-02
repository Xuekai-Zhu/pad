def solution():
    """A jewelry store is restocking its shelves. The necklace stand, which can hold 12 necklaces, currently holds 5 necklaces. The ring display, which can hold 30 rings, currently holds 18 rings. The bracelet display, which can hold 15 bracelets, currently holds 8 bracelets. The store’s supplier charges $4 per necklace, $10 per ring, and $5 per bracelet. How much, in dollars, will the store need to pay to fill the displays?"""
    necklace_stand = 12
    necklace_current = 5
    rings_display = 30
    rings_current = 18
    bracelet_display = 15
    bracelet_current = 8
    necklace_price = 4
    ring_price = 10
    bracelet_price = 5
    necklaces_needed = necklace_stand - necklace_current
    rings_needed = rings_display - rings_current
    bracelets_needed = bracelet_display - bracelet_current
    total_cost = (necklaces_needed * necklace_price) + (rings_needed * ring_price) + (bracelets_needed * bracelet_price)
    result = total_cost
    return result

print(solution())