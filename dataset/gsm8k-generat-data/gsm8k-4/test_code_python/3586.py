def solution():
    """Ernest bought 50 meters of wire and cut it into 5 equal parts. He then used 3 parts of the wire. How many meters of wire is not used?"""
    # Define the total length of wire
    total_length = 50

    # Divide the total length into 5 parts
    part_length = total_length / 5

    # Calculate the length of wire used
    used_length = part_length * 3

    # Calculate the length of wire not used
    not_used_length = total_length - used_length

    # Return the result
    result = not_used_length
    return result

print(solution())