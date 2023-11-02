def solution():
    total_wire = 50  # Ernest bought 50 meters of wire
    parts = 5  # Ernest cut the wire into 5 equal parts
    used_parts = 3  # Ernest used 3 parts of the wire

    # Calculate the length of each wire part
    part_length = total_wire / parts

    # Calculate the length of wire not used
    unused_wire_length = total_wire - (used_parts * part_length)
    result = unused_wire_length
    return result

print(solution())