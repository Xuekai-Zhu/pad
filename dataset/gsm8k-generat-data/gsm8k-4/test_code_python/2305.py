def solution():
    """A 40 meters rope was cut into 2 parts in the ratio of 2:3. How long is the shorter part?"""
    # Define the total length of the rope and the ratio of the parts
    total_length = 40
    ratio = [2, 3]

    # Calculate the total number of parts in the ratio
    total_parts = sum(ratio)

    # Calculate the length of each part
    part_length = total_length / total_parts

    # Calculate the length of the shorter part
    shorter_part_length = part_length * ratio[0]

    # return the result
    result = shorter_part_length
    return result

print(solution())