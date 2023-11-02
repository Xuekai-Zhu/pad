def solution():
    necklace_stand_capacity = 12
    ring_display_capacity = 30
    bracelet_display_capacity = 15

    current_necklaces = 5
    current_rings = 18
    current_bracelets = 8

    # Calculate the number of items needed to fill the displays
    necklaces_needed = necklace_stand_capacity - current_necklaces
    rings_needed = ring_display_capacity - current_rings
    bracelets_needed = bracelet_display_capacity - current_bracelets

    # Calculate the cost of filling the displays
    necklace_cost = necklaces_needed * 4
    ring_cost = rings_needed * 10
    bracelet_cost = bracelets_needed * 5
    total_cost = necklace_cost + ring_cost + bracelet_cost

    result = total_cost
    return result

print(solution())