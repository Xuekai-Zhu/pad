def solution():
    # Define the capacity and current items for each display
    necklace_capacity = 12
    ring_capacity = 30
    bracelet_capacity = 15
    current_necklaces = 5
    current_rings = 18
    current_bracelets = 8

    # Calculate the number of items needed for each display
    needed_necklaces = necklace_capacity - current_necklaces
    needed_rings = ring_capacity - current_rings
    needed_bracelets = bracelet_capacity - current_bracelets

    # Calculate the total cost of the items needed
    total_cost = needed_necklaces * 4 + needed_rings * 10 + needed_bracelets * 5
    result = total_cost
    return result

print(solution())