def solution():
    beads_per_necklace = 20
    beads_per_bracelet = 10
    beads_per_earring = 5

    num_necklaces_monday = 10
    num_necklaces_tuesday = 2
    num_bracelets_wednesday = 5
    num_earrings_wednesday = 7

    # Calculate the total number of beads used for all necklaces made
    total_necklace_beads = (num_necklaces_monday + num_necklaces_tuesday) * beads_per_necklace

    # Calculate the total number of beads used for all bracelets made
    total_bracelet_beads = num_bracelets_wednesday * beads_per_bracelet

    # Calculate the total number of beads used for all earrings made
    total_earring_beads = num_earrings_wednesday * beads_per_earring

    # Calculate the total number of beads used for all jewelry made
    total_beads = total_necklace_beads + total_bracelet_beads + total_earring_beads
    result = total_beads
    return result

print(solution())