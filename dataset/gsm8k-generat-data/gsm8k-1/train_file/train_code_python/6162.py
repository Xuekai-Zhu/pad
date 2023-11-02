def solution():
    """The sum of the three angles of a triangle equals 250. The left angle is twice the right angle's value, and the right angle is 60 degrees. Find the value of the top angle?"""
    right_angle = 60
    left_angle = 2 * right_angle
    sum_angles = right_angle + left_angle + top_angle
    top_angle = 180 - sum_angles
    result = top_angle
    return result

print(solution())