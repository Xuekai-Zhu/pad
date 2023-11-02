def solution():
    """Marnie makes bead bracelets. She bought 5 bags of 50 beads and 2 bags of 100 beads. If 50 beads are used to make one bracelet, how many bracelets will Marnie be able to make out of the beads she bought?"""
    # Define the number of beads per bag
    BEADS_PER_SMALL_BAG = 50
    BEADS_PER_LARGE_BAG = 100

    # Define the number of bags Marnie bought
    small_bags = 5
    large_bags = 2

    # Calculate the total number of small beads Marnie has
    total_small_beads = small_bags * BEADS_PER_SMALL_BAG

    # Calculate the total number of large beads Marnie has
    total_large_beads = large_bags * BEADS_PER_LARGE_BAG

    # Calculate the total number of beads Marnie has
    total_beads = total_small_beads + total_large_beads

    # Calculate the number of bracelets Marnie can make
    bracelets = total_beads // 50

    # Display the number of bracelets Marnie can make
    result = bracelets
    return result

print(solution())