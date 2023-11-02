def solution():
    """The area of a triangle with a given base and height is given by 1/2*base*height. What is the base length of a triangle with height 8 and area 24 square units?"""
    height = 8
    area = 24
    base = (2 * area) / height
    result = base
    return result

print(solution())