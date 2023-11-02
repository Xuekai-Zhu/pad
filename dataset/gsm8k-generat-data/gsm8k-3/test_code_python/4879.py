def solution():
    """Aliens and Martians have different numbers of limbs. Aliens have three arms and eight legs, while Martians have half as many legs and twice as many arms. How many more limbs will five aliens have than five Martians?"""
    # Define the number of arms and legs for aliens and Martians
    ALIEN_ARMS = 3
    ALIEN_LEGS = 8
    MARTIAN_ARMS = 6  # Twice as many as aliens
    MARTIAN_LEGS = 4  # Half as many as aliens

    # Calculate the total number of limbs for five aliens and five Martians
    alien_limbs = 5 * (ALIEN_ARMS + ALIEN_LEGS)
    martian_limbs = 5 * (MARTIAN_ARMS + MARTIAN_LEGS)

    # Find the difference in limbs between the two groups
    difference = alien_limbs - martian_limbs

    # Display the difference in limbs
    result = difference
    return result

print(solution())