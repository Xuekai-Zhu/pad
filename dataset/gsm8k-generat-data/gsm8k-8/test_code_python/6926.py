def solution():
    # Define the number of amethyst beads and calculate the number of amber beads
    amethyst_beads = 7
    amber_beads = 2 * amethyst_beads

    # Calculate the total number of amethyst and amber beads
    total_amethyst_and_amber = amethyst_beads + amber_beads

    # Calculate the number of turquoise beads
    turquoise_beads = 40 - total_amethyst_and_amber

    result = turquoise_beads
    return result

print(solution())