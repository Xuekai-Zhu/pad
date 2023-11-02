def solution():
    
    particles_after_walk = 331
    particles_left_behind = 223
    particles_before_swept = (particles_after_walk - particles_left_behind) * 10
    result = particles_before_swept
    return result

print(solution())