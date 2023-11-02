def solution():
    """Samuel swept the porch and cleared nine-tenths of the dust particles from it. As he walked across the porch afterward, his shoes left 223 dust particles behind. How many dust particles were on the porch before Samuel swept if there were 331 after he walked across it?"""
    # Define the number of dust particles after Samuel walked across the porch
    dust_particles_after = 331

    # Define the number of dust particles Samuel's shoes left behind
    shoes_particles = 223

    # Calculate the fraction of dust particles remaining after Samuel swept
    remaining_fraction = 1 - 0.9

    # Calculate the total number of dust particles before Samuel swept
    total_particles = (dust_particles_after + shoes_particles) / remaining_fraction

    result = total_particles
    return result

print(solution())