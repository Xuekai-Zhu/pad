def solution():
    # Calculate Carter's height in inches
    carter_height = 24 * 2  # Carter is twice as tall as his 24" tall dog

    # Calculate Betty's height in inches
    betty_height = carter_height - 12  # Betty is 12" shorter than Carter

    # Convert Betty's height from inches to feet
    betty_height_ft = betty_height / 12

    result = betty_height_ft
    return result

print(solution())