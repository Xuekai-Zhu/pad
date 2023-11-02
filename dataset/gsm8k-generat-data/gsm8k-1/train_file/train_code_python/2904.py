def solution():
    """A pen is longer than the rubber by 3 centimeters, and shorter than the pencil by 2 centimeters. Considering the pencil is 12 centimeters long, what is the total length of the rubber, the pen, and the pencil altogether?"""
    pencil_length = 12
    pen_length = pencil_length - 2
    rubber_length = pen_length - 3
    total_length = pencil_length + pen_length + rubber_length
    result = total_length
    return result

print(solution())