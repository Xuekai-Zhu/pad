def solution():
    """A 40-bead necklace is made up of three kinds of beads. There are seven amethyst beads and twice as many amber beads as amethysts. The third beads are turquoise. How many turquoise beads are in the necklace?"""
    amethyst_beads = 7
    amber_beads = 2 * amethyst_beads
    total_beads = 40
    turquoise_beads = total_beads - amethyst_beads - amber_beads
    result = turquoise_beads
    return result

print(solution())