def solution():
    """The area of a triangle with a given base and height is given by 1/2*base*height. What is the base length of a triangle with height 8 and area 24 square units?"""
    # Define the height and area of the triangle
    height = 8
    area = 24

    # Calculate the base length of the triangle
    base = (2 * area) / height

    # return the result
    result = base
    return result

print(solution())