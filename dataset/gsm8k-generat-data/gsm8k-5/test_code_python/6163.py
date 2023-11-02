def solution():
    right_angle = 60  # Given: the right angle is 60 degrees
    left_angle = 2 * right_angle  # Given: the left angle is twice the right angle's value
    total_angle = 250  # Given: the sum of the three angles of a triangle equals 250

    # Calculate the value of the top angle
    top_angle = total_angle - (right_angle + left_angle)

    result = top_angle
    return result

print(solution())