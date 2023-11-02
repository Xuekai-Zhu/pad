def solution():
    """In a triangle with angles A, B, and C, A is 60 degrees, and B is two times as big as C. Calculate the angle of B."""
    # Define angle A
    angle_A = 60

    # Calculate angle C
    angle_C = (180 - angle_A) / 3

    # Calculate angle B
    angle_B = 2 * angle_C

    result = angle_B
    return result

print(solution())