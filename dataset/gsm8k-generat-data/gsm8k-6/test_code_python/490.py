def solution():
    # Calculate the length of the third side of the triangle
    perimeter = 160  # given perimeter
    given_side1 = 40  # given side 1
    given_side2 = 50  # given side 2
    third_side = perimeter - given_side1 - given_side2  # calculate the length of the third side
    result = third_side
    return result

print(solution())