def solution():
    """The perimeter of a triangle is 160 cm. If two of the sides are 40 cm and 50 cm, calculate the length of the third side?"""
    # Define the first two sides
    side1 = 40
    side2 = 50

    # Calculate the perimeter of the triangle
    perimeter = 160

    # Calculate the third side
    side3 = perimeter - side1 - side2

    # Display the length of the third side
    result = side3
    return result

print(solution())