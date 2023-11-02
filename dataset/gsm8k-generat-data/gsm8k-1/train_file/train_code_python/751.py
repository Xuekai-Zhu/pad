def solution():
    """The length of a rectangle is four times its width. If the area is 100 m2. what is the length of the rectangle?"""
    area = 100
    width = area**(1/2)  # Since area = length * width and length = 4 * width, we can solve for width using the area and then find the length as 4 times the width
    length = 4 * width
    result = length
    return result

print(solution())