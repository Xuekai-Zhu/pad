def solution():
    # Calculate the number of limbs for each alien
    alien_limb_count = 3 + 8
    # Calculate the number of limbs for each Martian
    martian_limb_count = (2 * 3) + (0.5 * 8)
    # Calculate the difference in limb count between aliens and Martians
    limb_difference = (alien_limb_count * 5) - (martian_limb_count * 5)
    result = limb_difference
    return result

print(solution())