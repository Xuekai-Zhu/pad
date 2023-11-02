def solution():
    """A pen is longer than the rubber by 3 centimeters, and shorter than the pencil by 2 centimeters. Considering the pencil is 12 centimeters long, what is the total length of the rubber, the pen, and the pencil altogether?"""
    # Define the length of the pencil
    pencil_length = 12

    # Calculate the length of the pen
    pen_length = pencil_length + 2

    # Calculate the length of the rubber
    rubber_length = pen_length - 3

    # Calculate the total length of all three items
    total_length = pencil_length + pen_length + rubber_length

    # return the result
    result = total_length
    return result

print(solution())