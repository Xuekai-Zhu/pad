def solution():
    """There is a rectangle that is 4 inches wide. If the rectangle's perimeter is 30 inches, what is the area of the rectangle?"""
    # Define the width of the rectangle
    width = 4

    # Calculate the length of the rectangle
    length = (30 - 2 * width) / 2

    # Calculate the area of the rectangle
    area = length * width

    # return the result
    result = area
    return result

print(solution())