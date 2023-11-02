def solution():
    """There is a rectangle that is 4 inches wide. If the rectangle's perimeter is 30 inches, what is the area of the rectangle?"""
    width = 4
    perimeter = 30
    length = (perimeter - 2 * width) / 2
    area = length * width
    result = area
    return result

print(solution())