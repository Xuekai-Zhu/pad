def solution():
    # Define the length of the pencil
    pencil_length = 12

    # Calculate the length of the pen and the rubber
    pen_length = pencil_length - 2
    rubber_length = pen_length - 3

    # Calculate the total length of all three items
    total_length = pencil_length + pen_length + rubber_length
    result = total_length
    return result

print(solution())