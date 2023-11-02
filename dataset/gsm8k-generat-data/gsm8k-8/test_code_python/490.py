def solution():
    # Define the given sides
    side1 = 40
    side2 = 50

    # Calculate the perimeter and the sum of the given sides
    perimeter = 160
    sum_of_given_sides = side1 + side2

    # Calculate the length of the third side by subtracting the sum of the given sides from the perimeter
    third_side = perimeter - sum_of_given_sides

    result = third_side
    return result

print(solution())