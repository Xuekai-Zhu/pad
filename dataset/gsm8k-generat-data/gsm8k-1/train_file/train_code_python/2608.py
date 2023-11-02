def solution():
    """Nancy and Rose are making bracelets, and there are eight beads in each bracelet. Nancy has 40 metal beads and 20 more pearl beads. Rose has 20 crystal beads and twice as many stone beads as crystal beads. How many bracelets can Nancy and Rose make?"""
    metal_beads = 40
    pearl_beads = metal_beads + 20
    crystal_beads = 20
    stone_beads = 2 * crystal_beads
    total_beads = metal_beads + pearl_beads + crystal_beads + stone_beads
    bracelets = total_beads // 8
    result = bracelets
    return result

print(solution())