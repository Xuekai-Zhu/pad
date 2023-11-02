def solution():
    # Calculate the perimeter of the triangle
    perimeter = 160

    # Identify the length of the two known sides
    side1 = 40
    side2 = 50

    # Calculate the length of the third side
    side3 = perimeter - (side1 + side2)
    result = side3
    return result

print(solution())