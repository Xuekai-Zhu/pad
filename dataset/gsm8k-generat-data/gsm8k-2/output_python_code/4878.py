def solution():
    """Aliens and Martians have different numbers of limbs. Aliens have three arms and eight legs, while Martians have half as many legs and twice as many arms. How many more limbs will five aliens have than five Martians?"""
    alien_arms = 3
    alien_legs = 8
    martian_arms = 2 * alien_arms
    martian_legs = 0.5 * alien_legs
    five_alien_limbs = (5 * alien_arms) + (5 * alien_legs)
    five_martian_limbs = (5 * martian_arms) + (5 * martian_legs)
    difference = five_alien_limbs - five_martian_limbs
    result = difference
    return result

print(solution())