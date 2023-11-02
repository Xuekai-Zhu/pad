def solution():
    """Ernest bought 50 meters of wire and cut it into 5 equal parts. He then used 3 parts of the wire. How many meters of wire is not used?"""
    # Define the total length of wire bought and the number of parts it was cut into
    total_wire = 50
    num_parts = 5

    # Calculate the length of each part of wire
    part_length = total_wire / num_parts

    # Calculate the length of wire used
    used_length = part_length * 3

    # Calculate the length of wire not used
    not_used_length = total_wire - used_length

    # Display the length of wire not used
    result = not_used_length
    return result

print(solution())