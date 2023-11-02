def solution():
    """Samuel swept the porch and cleared nine-tenths of the dust particles from it. As he walked across the porch afterward, 
    his shoes left 223 dust particles behind. How many dust particles were on the porch before Samuel swept if there were 331 after he walked across it?"""
    dust_after_walking = 331
    dust_left_behind = 223
    total_dust_particles = dust_after_walking + dust_left_behind
    initial_dust_particles = total_dust_particles / (1 - 0.9)
    result = initial_dust_particles
    return result

print(solution())