def solution():
    """A bead shop sells one set of crystal beads at $9 each and one set of metal beads at $10 each. Nancy buys one set of crystal beads and two sets of metal beads. How much does she spend in all?"""
    crystal_beads_price = 9
    metal_beads_price = 10
    num_crystal_sets = 1
    num_metal_sets = 2
    total_spent = (crystal_beads_price * num_crystal_sets) + (metal_beads_price * num_metal_sets)
    result = total_spent
    return result

print(solution())