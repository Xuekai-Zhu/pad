def solution():
    
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