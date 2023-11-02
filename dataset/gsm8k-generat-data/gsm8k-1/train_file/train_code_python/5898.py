def solution():
    """Bailey is making a rectangle out of a 100cm length of rope he has. If the longer sides of the rectangle were 28cm long, what is the length of each of the shorter sides?"""
    total_length = 100
    longer_side = 28
    shorter_sides_combined = total_length - (2 * longer_side)
    shorter_side = shorter_sides_combined / 2
    result = shorter_side
    return result

print(solution())