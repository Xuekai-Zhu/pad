def solution():
    """John buys 3 spools of wire that are 20 feet each. It takes 4 feet to make a necklace. How many necklaces can he make?"""
    # Define the length of each spool of wire and the length required for each necklace
    spool_length = 20
    necklace_length = 4

    # Calculate the total wire length John has purchased
    total_length = spool_length * 3

    # Calculate the number of necklaces John can make
    num_necklaces = total_length // necklace_length

    #return the result
    result = num_necklaces
    return result

print(solution())