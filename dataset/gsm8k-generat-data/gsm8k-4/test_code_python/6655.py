def solution():
    """The three angles of a triangle add up to 180 degrees. The largest angle is 5 times bigger than the smallest. The middle angle is 3 times bigger than the smallest. How many degrees is the smallest angle?"""
    # Define the smallest angle
    smallest_angle = x

    # Define the largest and middle angles in terms of the smallest angle
    largest_angle = 5 * smallest_angle
    middle_angle = 3 * smallest_angle

    # Calculate the total angle of the triangle
    total_angle = smallest_angle + middle_angle + largest_angle

    # Check that the total angle is 180 degrees
    if total_angle == 180:
        result = smallest_angle
        return result
    else:
        # If the angles don't add up to 180, return an error message
        return "Error: Angles do not add up to 180 degrees."

print(solution())