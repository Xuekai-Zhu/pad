def solution():
    length = 24
    width = 6

    # Calculate the total area of the quilt
    total_area = length * width

    # Divide the total area by 4 to get the area of each side of the square
    square_area = total_area / 4

    # Calculate the length of each side of the square by taking the square root of the square area
    side_length = square_area ** 0.5
    result = side_length
    return result

print(solution())