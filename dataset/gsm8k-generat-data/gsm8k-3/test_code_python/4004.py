def solution():
    """John buys 3 spools of wire that are 20 feet each.  It takes 4 feet to make a necklace.  How many necklaces can he make?"""
    # Define the length of each spool of wire
    SPOOL_LENGTH = 20

    # Define the length needed to make one necklace
    NECKLACE_LENGTH = 4

    # Calculate the total length of wire John has
    total_wire_length = SPOOL_LENGTH * 3

    # Calculate how many necklaces John can make with the wire
    necklaces = total_wire_length // NECKLACE_LENGTH

    # Display the number of necklaces John can make
    result = necklaces
    return result

print(solution())