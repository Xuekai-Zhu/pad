def solution():
    """John buys 3 spools of wire that are 20 feet each. It takes 4 feet to make a necklace. How many necklaces can he make?"""
    spool_length = 20
    wire_needed_per_necklace = 4
    total_length = spool_length * 3
    necklaces = total_length // wire_needed_per_necklace
    result = necklaces
    return result

print(solution())