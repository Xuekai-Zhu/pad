def solution():
    """In a triangle with angles A, B, and C, A is 60 degrees, and B is two times as big as C. Calculate the angle of B."""
    angle_a = 60
    angle_b = 2 * angle_c
    angle_c = (180 - angle_a - angle_b) / 2
    result = angle_b
    return result

print(solution())