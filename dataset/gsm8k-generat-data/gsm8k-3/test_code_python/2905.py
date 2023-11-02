def solution():
    """A pen is longer than the rubber by 3 centimeters, and shorter than the pencil by 2 centimeters. Considering the pencil is 12 centimeters long, what is the total length of the rubber, the pen, and the pencil altogether?"""
    # Define the length of the pencil
    PENCIL_LENGTH = 12

    # Calculate the length of the pen
    pen_length = PENCIL_LENGTH - 2

    # Calculate the length of the rubber
    rubber_length = pen_length - 3

    # Calculate the total length of all three items
    total_length = PENCIL_LENGTH + pen_length + rubber_length

    # Display the total length
    result = total_length
    return result

print(solution())