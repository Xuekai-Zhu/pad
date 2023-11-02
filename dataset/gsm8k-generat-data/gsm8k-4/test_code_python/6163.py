def solution():
    """The sum of the three angles of a triangle equals 250. The left angle is twice the right angle's value, and the right angle is 60 degrees. Find the value of the top angle?"""
    # Define the value of the right angle
    right_angle = 60

    # Calculate the value of the left angle
    left_angle = 2 * right_angle

    # Calculate the sum of the three angles
    sum_angles = left_angle + right_angle + top_angle

    # Solve for the value of the top angle
    top_angle = 250 - left_angle - right_angle

    result = top_angle
    return result

print(solution())