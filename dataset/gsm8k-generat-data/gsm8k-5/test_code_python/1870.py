def solution():
    angle_A = 60  # Angle A is 60 degrees
    angle_B = 2 * angle_C  # Angle B is two times as big as angle C
    angle_C = (180 - angle_A - angle_B) / 2  # Calculate angle C using the fact that the sum of angles in a triangle is 180 degrees

    result = angle_B
    return result

print(solution())