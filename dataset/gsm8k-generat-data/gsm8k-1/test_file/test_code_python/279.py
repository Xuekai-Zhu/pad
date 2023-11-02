def solution():
    """Katerina makes designer jewelry. Her specialty is topaz necklaces. She uses 8 topaz gemstones per necklace, and fills the space between gemstones using sterling silver beads. If each topaz gemstone is one inch long, each sterling silver bead is one-quarter of an inch long, and each necklace is made to a total length of 25 inches, how many sterling silver beads does Katerina use per necklace?"""
    topaz_gemstones = 8
    topaz_length = 8    
    necklace_total_length = 25
    space_to_fill = necklace_total_length - topaz_length
    silver_bead_length = 0.25
    total_silver_beads = int(space_to_fill / silver_bead_length)
    result = total_silver_beads
    return result

print(solution())