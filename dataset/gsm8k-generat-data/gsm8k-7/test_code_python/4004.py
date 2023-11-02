def solution():
    num_spools = 3
    spool_length = 20  # feet
    necklace_length = 4  # feet

    # Calculate the total wire length in feet
    total_wire_length = num_spools * spool_length

    # Calculate the total number of necklaces he can make
    num_necklaces = total_wire_length // necklace_length
    result = num_necklaces
    return result

print(solution())