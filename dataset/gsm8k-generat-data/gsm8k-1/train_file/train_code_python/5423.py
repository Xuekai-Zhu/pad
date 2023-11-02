def solution():
    """A bead shop sells one set of crystal beads at $9 each and one set of metal beads at $10 each. Nancy buys one set of crystal beads and two sets of metal beads. How much does she spend in all?"""
    crystal_beads_price = 9
    metal_beads_price = 10
    crystal_beads_quantity = 1
    metal_beads_quantity = 2
    total_price = (crystal_beads_price * crystal_beads_quantity) + (metal_beads_price * metal_beads_quantity)
    result = total_price
    return result

print(solution())