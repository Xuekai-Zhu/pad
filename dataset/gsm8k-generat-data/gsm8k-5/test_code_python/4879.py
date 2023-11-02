def solution():
    # Limbs of one alien
    alien_arms = 3
    alien_legs = 8

    # Limbs of one martian
    martian_arms = 2 * alien_arms
    martian_legs = 0.5 * alien_legs

    # Total limbs of five aliens and five martians
    total_aliens = 5
    total_martians = 5
    limbs_aliens = total_aliens * (alien_arms + alien_legs)
    limbs_martians = total_martians * (martian_arms + martian_legs)

    # Calculate the difference
    difference = limbs_aliens - limbs_martians
    result = difference
    return result

print(solution())