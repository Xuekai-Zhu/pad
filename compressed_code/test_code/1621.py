def solution():
    
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