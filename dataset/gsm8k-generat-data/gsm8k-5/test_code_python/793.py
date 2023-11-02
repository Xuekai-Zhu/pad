def solution():
    width = 4  # The width of the rectangle is 4 inches
    perimeter = 30  # The perimeter of the rectangle is 30 inches
    length = (perimeter - 2 * width) / 2  # Calculate the length of the rectangle using the perimeter formula

    # Calculate the area of the rectangle
    area = length * width
    result = area
    return result

print(solution())