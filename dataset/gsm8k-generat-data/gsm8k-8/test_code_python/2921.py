def solution():
    # Define the fraction of times Martin rings the big bell
    big_bell_fraction = x

    # Calculate how many times Martin rings the small bell
    small_bell_times = 4 + (1/3)*big_bell_fraction
    # Calculate how many times Martin rings both bells combined
    total_rings = 52
    # Solve the system of equations to find x and y
    x = 3/(10-small_bell_times)
    y = total_rings - small_bell_times - x

    # Calculate how many times Martin rings the big bell
    big_bell_times = big_bell_fraction * y
    result = big_bell_times
    return result

print(solution())