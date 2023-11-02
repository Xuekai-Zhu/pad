def solution():
    # Define the left and right sides of the triangle
    left_side = 12
    right_side = left_side + 2

    # Calculate the value of the third side
    third_side = 50 - (left_side + right_side)

    # Return the value of the third side
    result = third_side
    return result

print(solution())