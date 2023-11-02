def solution():
    total_wire = 50
    num_parts = 5
    used_parts = 3

    # Calculate the length of each wire part
    part_length = total_wire / num_parts

    # Calculate the total length of the used wire
    used_length = used_parts * part_length

    # Calculate the length of the wire that is not used
    not_used_length = total_wire - used_length
    result = not_used_length
    return result

print(solution())