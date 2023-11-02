def solution():
    """John buys 3 spools of wire that are 20 feet each. It takes 4 feet to make a necklace. How many necklaces can he make?"""
    spool_length = 20
    wire_length = spool_length * 3
    necklace_length = 4
    num_necklaces = wire_length // necklace_length
    result = num_necklaces
    return result

print(solution())