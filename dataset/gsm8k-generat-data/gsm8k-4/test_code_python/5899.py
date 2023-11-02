def solution():
    """Bailey is making a rectangle out of a 100cm length of rope he has. If the longer sides of the rectangle were 28cm long, what is the length of each of the shorter sides?"""
    # Define the total length of the rope
    total_length = 100

    # Define the length of one pair of sides
    long_side = 28
    short_side = (total_length - 2*long_side) / 2

    # return the result
    result = short_side
    return result

print(solution())