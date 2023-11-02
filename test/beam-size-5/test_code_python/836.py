def solution():
    # Calculate the total length of the glue sticks that are not used
    used_length = (1/6) * 12 + (2/3) * 12 + (1/2) * 12  # the first stick is 12 millimeters long, the second stick is 2/3 left, and the third stick is 1/2 left
    # Calculate the total length of the glue sticks that are not used
    not_used_length = 12 - used_length
    result = not_used_length
    return result

print(solution())