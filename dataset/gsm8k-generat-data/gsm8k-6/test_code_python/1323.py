def solution():
    # Calculate the area of the quilt
    area = 6 * 24  

    # Calculate the length of each side of the square
    side_length = (area ** 0.5) / 2  # square root of area divided by 2 to get the length of a side
    result = side_length
    return result

print(solution())