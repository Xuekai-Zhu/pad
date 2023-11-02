def solution():
    # Calculate the angle of C
    angle_C = (180 - 60) / 3  # the sum of angles in a triangle is 180 degrees, and A is 60 degrees
    # Calculate the angle of B, which is two times as big as C
    angle_B = 2 * angle_C
    result = angle_B
    return result

print(solution())