def solution():
    angle_A = 60
    angle_B = 0
    angle_C = 0

    # Use the fact that the sum of the angles in a triangle is 180 degrees
    angle_C = (180 - angle_A) / 3
    angle_B = 2 * angle_C

    result = angle_B
    return result

print(solution())