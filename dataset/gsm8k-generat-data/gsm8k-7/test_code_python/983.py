def solution():
    dog_height = 24
    carter_height = 2 * dog_height
    betty_height = carter_height - 12

    # Convert height from inches to feet
    betty_height_feet = betty_height / 12
    result = betty_height_feet
    return result

print(solution())