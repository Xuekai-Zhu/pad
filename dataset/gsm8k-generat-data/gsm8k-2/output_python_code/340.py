def solution():
    """Samuel swept the porch and cleared nine-tenths of the dust particles from it. As he walked across the porch afterward, his shoes left 223 dust particles behind. How many dust particles were on the porch before Samuel swept if there were 331 after he walked across it?"""
    particles_after_walk = 331
    particles_left_behind = 223
    particles_before_swept = (particles_after_walk - particles_left_behind) * 10
    result = particles_before_swept
    return result

print(solution())