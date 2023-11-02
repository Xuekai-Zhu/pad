def solution():
    """Carter is twice as tall as his 24” tall dog. Betty is 12” shorter than Carter. How tall is Betty in feet?"""
    # Define the height of the dog
    dog_height = 24

    # Calculate Carter's height
    carter_height = dog_height * 2

    # Calculate Betty's height
    betty_height = carter_height - 12

    # Convert Betty's height from inches to feet
    betty_height_feet = betty_height / 12
    
    # Return Betty's height in feet
    result = betty_height_feet
    return result

print(solution())