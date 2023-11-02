def solution():
    """Samuel swept the porch and cleared nine-tenths of the dust particles from it. As he walked across the porch afterward, his shoes left 223 dust particles behind. How many dust particles were on the porch before Samuel swept if there were 331 after he walked across it?"""
    # Define the number of dust particles left by Samuel's shoes
    shoes_particles = 223

    # Define the total number of particles after Samuel walked across the porch
    total_particles_after = 331

    # Calculate the number of particles cleared by Samuel
    particles_cleared = total_particles_after - shoes_particles

    # Calculate the total number of particles before Samuel swept
    total_particles_before = particles_cleared / (1 - 0.9)

    # Display the total number of particles before Samuel swept
    result = total_particles_before
    return result

print(solution())