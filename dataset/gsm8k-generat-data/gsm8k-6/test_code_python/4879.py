def solution():
    # Calculate the total number of limbs for one alien and one Martian
    alien_limbs = 3 + 8  # alien has 3 arms and 8 legs
    martian_limbs = 2 * 3 + (8 / 2)  # Martian has twice as many arms as alien, and half as many legs

    # Calculate the total number of limbs for five aliens and five Martians
    total_alien_limbs = 5 * alien_limbs
    total_martian_limbs = 5 * martian_limbs

    # Calculate the difference in the total number of limbs between the five aliens and five Martians
    diff = total_alien_limbs - total_martian_limbs
    result = diff
    return result

print(solution())