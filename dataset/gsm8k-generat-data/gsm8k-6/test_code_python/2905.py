def solution():
    # Calculate the length of the pen and the rubber
    pen_length = 12 - 2  # the pen is 2 cm shorter than the pencil
    rubber_length = pen_length - 3  # the rubber is 3 cm shorter than the pen

    # Calculate the total length of the three items
    total_length = pen_length + rubber_length + 12  # 12 is the length of the pencil
    result = total_length
    return result

print(solution())