def solution():
    # Calculate how much velvet is needed for one cloak
    velvet_for_cloak = 3  # three yards of velvet needed to make one cloak

    # Calculate how much velvet is needed for one hat
    velvet_for_hat = 1/4  # one yard of velvet makes 4 hats

    # Calculate how much velvet is needed for 6 cloaks
    velvet_for_6_cloaks = 6 * velvet_for_cloak

    # Calculate how much velvet is needed for 12 hats
    velvet_for_12_hats = 12 * velvet_for_hat

    # Calculate the total amount of velvet needed
    total_velvet_needed = velvet_for_6_cloaks + velvet_for_12_hats

    result = total_velvet_needed
    return result

print(solution())