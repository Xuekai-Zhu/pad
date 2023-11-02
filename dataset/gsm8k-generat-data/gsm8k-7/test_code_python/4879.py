def solution():
    num_aliens = 5
    num_martians = 5

    # Calculate the total number of limbs for the five aliens
    aliens_limbs = (num_aliens * 3) + (num_aliens * 8)

    # Calculate the total number of limbs for the five Martians
    martians_arms = num_martians * 2
    martians_legs = num_martians * 8 / 2
    martians_limbs = martians_arms + martians_legs

    # Calculate the difference in limbs between the aliens and Martians
    limb_difference = aliens_limbs - martians_limbs
    result = limb_difference
    return result

print(solution())