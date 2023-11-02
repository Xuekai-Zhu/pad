def solution():
    # Calculate the total number of rubber bands
    total_bands = 6 * 3

    # Let x be the number of bands that Joe has
    x = (total_bands - 1)/3

    # Let y be the number of bands that Aira has
    y = x - 1

    # Let z be the number of bands that Samantha has
    z = y + 5

    # Return the number of bands that Aira has
    return y

print(solution())