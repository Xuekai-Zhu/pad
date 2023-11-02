def solution():
    
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