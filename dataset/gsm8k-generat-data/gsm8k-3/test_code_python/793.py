def solution():
    """There is a rectangle that is 4 inches wide. If the rectangle's perimeter is 30 inches, what is the area of the rectangle?"""
    # Define the width of the rectangle
    width = 4

    # Calculate the length of the rectangle
    perimeter = 30
    length = (perimeter - 2 * width) / 2

    # Calculate the area of the rectangle
    area = width * length

    # Display the area of the rectangle
    result = area
    return result

print(solution())