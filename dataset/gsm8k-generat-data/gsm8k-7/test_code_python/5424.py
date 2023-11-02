def solution():
    crystal_beads_price = 9
    metal_beads_price = 10
    num_crystal_beads_sets = 1
    num_metal_beads_sets = 2

    # Calculate the total cost of crystal beads
    total_crystal_beads_cost = num_crystal_beads_sets * crystal_beads_price

    # Calculate the total cost of metal beads
    total_metal_beads_cost = num_metal_beads_sets * metal_beads_price

    # Calculate the total cost of all bead sets
    total_cost = total_crystal_beads_cost + total_metal_beads_cost
    result = total_cost
    return result

print(solution())