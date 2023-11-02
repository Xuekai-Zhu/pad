def solution():
    """The length of a rectangle is four times its width. If the area is 100 m2. what is the length of the rectangle?"""
    area = 100
    ratio = 4
    width = (area / ratio) ** 0.5
    length = ratio * width
    result = length
    return result

print(solution())