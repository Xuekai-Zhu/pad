def solution():
    spools_of_wire = 3  # number of spools of wire
    length_of_wire = 20 * spools_of_wire  # total length of wire in feet
    length_of_necklace = 4  # length of wire needed to make a necklace
    total_necklaces = length_of_wire // length_of_necklace  # total number of necklaces that can be made
    result = total_necklaces
    return result

print(solution())