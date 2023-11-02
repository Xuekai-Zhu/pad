def solution():
    perimeter = 160
    side1 = 40
    side2 = 50

    # Calculate the sum of the two known sides
    known_sides_sum = side1 + side2

    # Calculate the length of the third side
    third_side = perimeter - known_sides_sum

    result = third_side
    return result

print(solution())