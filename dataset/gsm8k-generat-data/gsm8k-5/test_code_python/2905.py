def solution():
    pencil_length = 12  # Given, pencil length is 12cm
    pen_length = pencil_length - 2  # Pen is 2cm shorter than pencil
    rubber_length = pen_length - 3  # Rubber is 3cm shorter than pen

    # Calculate total length of all items
    total_length = pencil_length + pen_length + rubber_length
    result = total_length
    return result

print(solution())