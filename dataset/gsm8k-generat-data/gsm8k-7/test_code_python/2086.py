def solution():
    # Define the capacity and current inventory of each display
    necklace_capacity = 12
    necklace_inventory = 5

    ring_capacity = 30
    ring_inventory = 18

    bracelet_capacity = 15
    bracelet_inventory = 8

    # Define the cost of each piece of jewelry
    necklace_cost = 4
    ring_cost = 10
    bracelet_cost = 5

    # Calculate the number of items needed to fill each display
    num_necklaces_needed = necklace_capacity - necklace_inventory
    num_rings_needed = ring_capacity - ring_inventory
    num_bracelets_needed = bracelet_capacity - bracelet_inventory

    # Calculate the cost of filling each display
    necklace_cost_total = num_necklaces_needed * necklace_cost
    ring_cost_total = num_rings_needed * ring_cost
    bracelet_cost_total = num_bracelets_needed * bracelet_cost

    # Calculate the total cost of restocking the displays
    total_cost = necklace_cost_total + ring_cost_total + bracelet_cost_total
    result = total_cost
    return result

print(solution())