def solution():
    width = 4
    perimeter = 30

    # Calculate the length of the rectangle using the perimeter equation
    length = (perimeter - 2*width) / 2

    # Calculate the area of the rectangle
    area = width * length
    result = area
    return result

print(solution())