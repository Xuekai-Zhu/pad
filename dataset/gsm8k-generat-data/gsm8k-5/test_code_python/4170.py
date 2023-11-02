def solution():
    total_marbles = 215  # Amon and Rhonda have a combined total of 215 marbles
    difference = 55  # Amon owns 55 more marbles than Rhonda

    # Set up a system of equations:
    # A + R = 215 (total number of marbles)
    # A = R + 55 (Amon owns 55 more marbles than Rhonda)
    # Substitute A = R + 55 into the first equation and solve for R
    # (R + 55) + R = 215
    # 2R = 160
    # R = 80

    # Calculate how many marbles Rhonda has
    rhonda_marbles = 80
    result = rhonda_marbles
    return result

print(solution())