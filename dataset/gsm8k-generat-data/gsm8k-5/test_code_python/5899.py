def solution():
    total_length = 100  # Bailey has a 100cm length of rope
    longer_sides = 28  # The longer sides of the rectangle are 28cm long
    remaining_length = total_length - (2 * longer_sides)  # Bailey will use 2 * longer_sides of the rope for the longer sides of the rectangle
    shorter_sides = remaining_length / 2  # Divide the remaining length by 2 for the length of each shorter side
    result = shorter_sides
    return result

print(solution())