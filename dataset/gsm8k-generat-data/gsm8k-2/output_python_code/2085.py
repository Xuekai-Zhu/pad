def solution():
    """A jewelry store is restocking its shelves. The necklace stand, which can hold 12 necklaces, currently holds 5 necklaces. The ring display, which can hold 30 rings, currently holds 18 rings. The bracelet display, which can hold 15 bracelets, currently holds 8 bracelets. The store’s supplier charges $4 per necklace, $10 per ring, and $5 per bracelet. How much, in dollars, will the store need to pay to fill the displays?"""
    necklace_stand_capacity = 12
    ring_display_capacity = 30
    bracelet_display_capacity = 15
    current_necklaces = 5
    current_rings = 18
    current_bracelets = 8
    necklace_price = 4
    ring_price = 10
    bracelet_price = 5

    remaining_necklaces = necklace_stand_capacity - current_necklaces
    remaining_rings = ring_display_capacity - current_rings
    remaining_bracelets = bracelet_display_capacity - current_bracelets

    total_cost = remaining_necklaces * necklace_price + remaining_rings * ring_price + remaining_bracelets * bracelet_price
    result = total_cost
    return result

print(solution())