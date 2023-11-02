def solution():
    """The length of a rectangle is four times its width. If the area is 100 m2. what is the length of the rectangle?"""
    # Define the area of the rectangle
    area = 100

    # Find the width of the rectangle
    width = (area/4)**0.5

    # Find the length of the rectangle
    length = 4 * width

    # Display the length of the rectangle
    result = length
    return result

print(solution())