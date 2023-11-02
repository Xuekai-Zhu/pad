def solution():
    # Calculate the number of dust particles on the porch before Samuel swept
    total_dust_particles = 331 - 223  # number of dust particles after Samuel walked minus the number he left behind
    before_swept = total_dust_particles / (1 - 9/10)  # nine-tenths of the dust particles were cleared by Samuel
    result = before_swept
    return result

print(solution())