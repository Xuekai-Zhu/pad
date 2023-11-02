def solution():
    """A Printing shop needs to ship 5000 brochures to an advertising company. Each box can only contain one-fifth of the brochures. How many boxes are needed to ship those brochures?"""
    brochures = 5000
    box_capacity = brochures / 5
    boxes_needed = brochures // box_capacity
    if brochures % box_capacity != 0:
        boxes_needed += 1
    result = boxes_needed
    return result

print(solution())