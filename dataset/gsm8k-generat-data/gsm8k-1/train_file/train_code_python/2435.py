def solution():
    """A Printing shop needs to ship 5000 brochures to an advertising company. Each box can only contain one-fifth of the brochures. How many boxes are needed to ship those brochures?"""
    total_brochures = 5000
    brochures_per_box = total_brochures / 5
    boxes_needed = total_brochures / brochures_per_box
    result = boxes_needed
    return result

print(solution())