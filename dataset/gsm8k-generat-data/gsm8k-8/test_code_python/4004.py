def solution():
    # Define the length of each spool of wire
    wire_length = 20

    # Calculate the total length of wire John has
    total_wire_length = wire_length * 3

    # Calculate the length of wire needed to make one necklace
    necklace_length = 4

    # Calculate the number of necklaces John can make
    num_of_necklaces = total_wire_length // necklace_length
    result = num_of_necklaces
    return result

print(solution())