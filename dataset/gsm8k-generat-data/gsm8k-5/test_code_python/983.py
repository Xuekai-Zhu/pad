def solution():
    dog_height = 24 # Carter's dog is 24 inches tall
    carter_height = 2 * dog_height # Carter is twice as tall as his dog
    betty_height = carter_height - 12 # Betty is 12 inches shorter than Carter

    # Convert Betty's height from inches to feet
    betty_height_feet = betty_height / 12
    result = betty_height_feet
    return result

print(solution())