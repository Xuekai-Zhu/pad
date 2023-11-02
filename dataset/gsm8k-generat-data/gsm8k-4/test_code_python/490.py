def solution():
    """The perimeter of a triangle is 160 cm. If two of the sides are 40 cm and 50 cm, calculate the length of the third side?"""
    # Define the perimeter and two sides
    perimeter = 160
    side1 = 40
    side2 = 50

    # Calculate the sum of the two known sides
    sum_of_sides = side1 + side2

    # Calculate the length of the third side
    third_side = perimeter - sum_of_sides

    # Return the result
    result = third_side
    return result

print(solution())