def solution():
    """Nancy and Rose are making bracelets, and there are eight beads in each bracelet.  Nancy has 40 metal beads and 20 more pearl beads. Rose has 20 crystal beads and twice as many stone beads as crystal beads. How many bracelets can Nancy and Rose make?"""
    # Define the number of beads needed for each bracelet
    BEADS_PER_BRACELET = 8

    # Calculate the total number of beads Nancy has
    nancy_beads = 40 + 20

    # Calculate the total number of beads Rose has
    rose_beads = 20 + 2 * 20

    # Calculate the total number of bracelets they can make
    total_bracelets = (nancy_beads + rose_beads) // BEADS_PER_BRACELET

    # Display the total number of bracelets they can make
    result = total_bracelets
    return result

print(solution())