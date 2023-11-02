def solution():
    # Calculate the number of dust particles Samuel cleared
    cleared_particles = 9/10

    # Calculate the total number of dust particles on the porch before Samuel swept
    total_particles_before = (331 - 223) / (1 - cleared_particles)

    result = total_particles_before
    return result

print(solution())