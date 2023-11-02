def solution():
    """A long wire is cut into three smaller pieces in the ratio of 7:3:2. If the shortest piece is 16 cm, how long was the entire wire before it was cut?"""
    # Define the ratio of the three smaller pieces
    ratio = [7, 3, 2]

    # Calculate the total number of parts in the ratio
    total_parts = sum(ratio)

    # Calculate the length of each part
    part_length = 16 / ratio[2]

    # Calculate the length of the entire wire
    wire_length = part_length * total_parts

    result = wire_length
    return result

print(solution())