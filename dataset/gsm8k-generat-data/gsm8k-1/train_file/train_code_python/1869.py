def solution():
    """In a triangle with angles A, B, and C, A is 60 degrees, and B is two times as big as C. Calculate the angle of B."""
    angle_a = 60
    angle_c = (180 - angle_a)/3
    angle_b = 2 * angle_c
    result = angle_b
    return result

print(solution())