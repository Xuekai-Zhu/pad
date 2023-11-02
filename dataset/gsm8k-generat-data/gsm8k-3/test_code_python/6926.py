def solution():
    """A 40-bead necklace is made up of three kinds of beads. There are seven amethyst beads and twice as many amber beads as amethysts. The third beads are turquoise. How many turquoise beads are in the necklace?"""
    # Define the number of amethyst and amber beads
    amethyst_beads = 7
    amber_beads = 2 * amethyst_beads

    # Calculate the number of turquoise beads
    turquoise_beads = 40 - amethyst_beads - amber_beads

    # Display the number of turquoise beads
    result = turquoise_beads
    return result

print(solution())