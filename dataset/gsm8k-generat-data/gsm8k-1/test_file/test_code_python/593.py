def solution():
    """The three angles in a triangle add up to 180 degrees. One angle is twice the smallest angle, and one angle is three times the smallest angle. What is the measure of the largest angle in the triangle, in degrees?"""
    smallest_angle = 1
    angle1 = 2 * smallest_angle
    angle2 = 3 * smallest_angle
    largest_angle = 180 - smallest_angle - angle1 - angle2
    result = largest_angle
    return result

print(solution())