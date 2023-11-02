def solution():
    # Total number of dust particles after sweeping
    total_after_sweeping = 331

    # Number of particles left after Samuel walked across
    particles_remaining = 223

    # Proportion of dust particles cleared during sweeping
    proportion_cleared = 0.9

    # Calculate the total number of dust particles before Samuel swept
    total_before_sweeping = (total_after_sweeping - particles_remaining) / proportion_cleared
    result = total_before_sweeping
    return result

print(solution())