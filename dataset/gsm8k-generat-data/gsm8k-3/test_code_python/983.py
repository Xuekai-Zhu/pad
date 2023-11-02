def solution():
    """Carter is twice as tall as his 24” tall dog.  Betty is 12” shorter than Carter.  How tall is Betty in feet?"""
    # Calculate Carter's height in inches
    carter_height = 2 * 24

    # Calculate Betty's height in inches
    betty_height = carter_height - 12

    # Convert Betty's height to feet
    betty_height_in_feet = betty_height / 12

    # Display Betty's height in feet
    result = betty_height_in_feet
    return result

print(solution())