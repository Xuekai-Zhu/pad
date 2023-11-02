def solution():
    """Carter is twice as tall as his 24” tall dog. Betty is 12” shorter than Carter. How tall is Betty in feet?"""
    dog_height = 24
    carter_height = 2 * dog_height
    betty_height = carter_height - 12
    betty_height_feet = betty_height / 12
    result = betty_height_feet
    return result

print(solution())