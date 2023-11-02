def solution():
    # Define the length of the longer sides and the total length of the rope
    longer_sides = 28
    total_length = 100

    # Calculate the length of the shorter sides
    shorter_sides = (total_length - 2 * longer_sides) / 2

    result = shorter_sides
    return result

print(solution())