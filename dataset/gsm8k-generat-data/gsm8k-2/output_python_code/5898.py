def solution():
    """Bailey is making a rectangle out of a 100cm length of rope he has. If the longer sides of the rectangle were 28cm long, what is the length of each of the shorter sides?"""
    rope_length = 100
    long_side = 28
    short_side = (rope_length - 2 * long_side) / 2
    result = short_side
    return result

print(solution())