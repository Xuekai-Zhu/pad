def solution():
    # Calculate the length of the bathroom before extension
    length = 96 / 8  # width x length = area -> length = area / width

    # Calculate the new width and length after extension
    new_width = 8 + 2 + 2  # 2 feet added on each side
    new_length = length

    # Calculate the new area of the bathroom
    new_area = new_width * new_length
    result = new_area
    return result

print(solution())