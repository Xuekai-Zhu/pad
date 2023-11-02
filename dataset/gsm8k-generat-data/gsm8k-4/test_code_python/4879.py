def solution():
    """Aliens and Martians have different numbers of limbs. Aliens have three arms and eight legs, while Martians have half as many legs and twice as many arms. How many more limbs will five aliens have than five Martians?"""
    # Define the number of limbs for one alien and one Martian
    alien_limbs = 3 + 8
    martian_limbs = 2 * 3 + 0.5 * 8

    # Calculate the total number of limbs for five aliens and five Martians
    total_alien_limbs = alien_limbs * 5
    total_martian_limbs = martian_limbs * 5

    # Calculate the difference in number of limbs between the two groups
    limb_difference = total_alien_limbs - total_martian_limbs

    # Return the result
    result = limb_difference
    return result

print(solution())