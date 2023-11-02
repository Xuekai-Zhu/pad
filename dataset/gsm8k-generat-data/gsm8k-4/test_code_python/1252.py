def solution():
    """Marnie makes bead bracelets. She bought 5 bags of 50 beads and 2 bags of 100 beads. If 50 beads are used to make one bracelet, how many bracelets will Marnie be able to make out of the beads she bought?"""
    # Define the number of beads in each bag
    bag1 = 50
    bag2 = 100

    # Define the number of bags of beads
    bags_of_bag1 = 5
    bags_of_bag2 = 2

    # Calculate the total number of beads
    total_beads = (bag1 * bags_of_bag1) + (bag2 * bags_of_bag2)

    # Calculate the number of bracelets that can be made
    bracelets = total_beads // 50

    # return the result
    result = bracelets
    return result

print(solution())