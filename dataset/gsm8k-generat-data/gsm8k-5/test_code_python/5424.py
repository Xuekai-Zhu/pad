def solution():
    crystal_bead_price = 9  # Price of one set of crystal beads
    metal_bead_price = 10  # Price of one set of metal beads
    nancy_crystal_beads = 1  # Nancy buys one set of crystal beads
    nancy_metal_beads = 2  # Nancy buys two sets of metal beads

    # Calculate the total amount Nancy spends
    total_spent = (crystal_bead_price * nancy_crystal_beads) + (metal_bead_price * nancy_metal_beads)
    result = total_spent
    return result

print(solution())