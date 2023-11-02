def solution():
    topaz_gemstones_per_necklace = 8  # Katerina uses 8 topaz gemstones per necklace
    sterling_beads_per_inch = 0.25  # Each sterling silver bead is one-quarter of an inch long
    total_inches = 25  # Katerina's specialty is made to a total length of 25 inches

    # Calculate the total number of sterling silver beads used per necklace
    sterling_beads_per_necklace = (total_inches - (topaz_gemstones_per_necklace * sterling_beads_per_inch)) / sterling_beads_per_necklace
    result = sterling_beads_per_necklace
    return result

print(solution())