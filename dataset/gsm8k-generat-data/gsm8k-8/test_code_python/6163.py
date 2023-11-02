def solution():
    # Define the value of the right angle
    right_angle = 60

    # Calculate the value of the left angle
    left_angle = 2 * right_angle

    # Calculate the value of the top angle
    top_angle = 250 - (left_angle + right_angle)

    result = top_angle
    return result

print(solution())